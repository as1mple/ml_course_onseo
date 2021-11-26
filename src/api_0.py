from fastapi import FastAPI
from loguru import logger

from .modules.data_models import Message

DEFAULT_RESPONSES = {500: {'model': Message}}

logger.add('deb  ug.log', format="{time} {level} {message}", level="DEBUG", rotation="1 weeks", compression='zip')

app = FastAPI()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check")
    return Message(message="Success")

