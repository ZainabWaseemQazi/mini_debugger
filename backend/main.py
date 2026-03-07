from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from core.middleware import RequestMiddleware
from core.exception_handler import global_exception_handler
from core.logger import setup_logger
from core.config import settings

from schemas.request import CodeRequest
from schemas.response import CodeResponse

from db.database import SessionLocal, engine
from db.models import Base, DebugHistory

from llm.llm_wrapper import LLMWrapper
from agents.debug_agent import DebugAgent
from sandbox.executor import DockerExecutor
from orchestrator import CodeOrchestrator

# --------------------------------------------------
# Logger Setup
# --------------------------------------------------
logger = setup_logger()

# --------------------------------------------------
# FastAPI App Initialization
# --------------------------------------------------
app = FastAPI(title="AI Debugger API", version="1.0.0")

#cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(RequestMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

# --------------------------------------------------
# Database Initialization (Create Tables)
# --------------------------------------------------
Base.metadata.create_all(bind=engine)

# --------------------------------------------------
# Dependency: DB Session
# --------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------------------------------
# Initialize Core Components
# --------------------------------------------------
llm = LLMWrapper()
executor = DockerExecutor()
debug_agent = DebugAgent(llm)

orchestrator = CodeOrchestrator(
    executor=executor,
    debug_agent=debug_agent,
    max_candidates=settings.MAX_ITERATIONS
)

# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------
@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "AI Debugger Running"}

# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# --------------------------------------------------
# Review & Debug Endpoint
# --------------------------------------------------
@app.post("/review_debug", response_model=CodeResponse)
def review_and_debug(request: CodeRequest, db: Session = Depends(get_db)):

    logger.info("Review-debug endpoint hit")

    # Run AI Debug Orchestrator
    result = orchestrator.run(request.code)

    # Save History in Database
    history_entry = DebugHistory(
        original_code=request.code,
        final_code=result.get("final_code"),
        iterations=result.get("iterations"),
        success=result.get("success"),
        status=result.get("status")
    )

    db.add(history_entry)
    db.commit()

    logger.info(f"Debug session stored in DB (Success={result.get('success')})")

    return result