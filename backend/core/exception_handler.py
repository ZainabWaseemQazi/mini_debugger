from fastapi import Request
from fastapi.responses import JSONResponse
from core.logger import setup_logger

logger = setup_logger()


async def global_exception_handler(request: Request, exc: Exception):
    request_id = getattr(request.state, "request_id", "unknown")

    logger.error(
        f"[{request_id}] Internal Server Error: {str(exc)}",
        exc_info=True
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "request_id": request_id
        }
    )