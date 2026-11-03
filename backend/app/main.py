import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging
from app.core.exception_handlers import global_exception_handler
from app.api.routes.health import router as health_router


# Initialize logging
setup_logging()

logger = logging.getLogger(__name__)


# Application lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("SlideForge AI application started")

    yield

    logger.info("SlideForge AI application stopped")


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered academic presentation generator",
    version="1.0.0",
    debug=False,
    lifespan=lifespan
)


# Register global exception handler
app.add_exception_handler(
    Exception,
    global_exception_handler
)


# Register API routes
app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to SlideForge AI API",
        "status": "running",
        "environment": settings.APP_ENV
    }
