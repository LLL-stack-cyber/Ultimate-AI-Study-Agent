from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.student import router as student_router
from app.api.teacher import router as teacher_router
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.services.file_processing import FileProcessingService

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    setup_logging(settings.log_level)
    FileProcessingService.ensure_storage_dir(settings.storage_path)
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(student_router, prefix="/api/v1")
app.include_router(teacher_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name, "env": settings.app_env}
