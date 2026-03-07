import uuid
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from core.logger import setup_logger

logger = setup_logger()


class RequestMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        start_time = time.time()

        logger.info(
            f"[{request_id}] Incoming request: {request.method} {request.url.path}"
        )

        try:
            response = await call_next(request)

        except Exception as e:
            logger.error(f"[{request_id}] Unhandled exception: {str(e)}", exc_info=True)
            raise e

        process_time = round(time.time() - start_time, 4)

        logger.info(
            f"[{request_id}] Completed in {process_time}s | Status {response.status_code}"
        )

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(process_time)

        return response