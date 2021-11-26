from fastapi import FastAPI
from fastapi.responses import JSONResponse
from loguru import logger

from .modules.data_models import Message
from .modules.data_models import RequestText, ResponseSentiment
from .modules.simple_ml_models import SentimentModel

DEFAULT_RESPONSES = {500: {'model': Message}}

logger.add('deb  ug.log', format="{time} {level} {message}", level="DEBUG", rotation="1 weeks", compression='zip')

app = FastAPI()
app.model = SentimentModel()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check")
    return Message(message="Success")


@app.post("/api/v1/sentiment", response_model=ResponseSentiment, responses={**DEFAULT_RESPONSES})
def calc_sum(text: RequestText):
    logger.info("Sentiment")

    try:

        sentiment = app.model(text=text.text)
        return ResponseSentiment(**sentiment)

    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})
