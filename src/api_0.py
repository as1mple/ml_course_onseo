from fastapi import FastAPI
from fastapi.responses import JSONResponse
from loguru import logger

from .modules.data_models import Message, RequestCalc, ResponseCalc

DEFAULT_RESPONSES = {500: {'model': Message}}

logger.add('deb  ug.log', format="{time} {level} {message}", level="DEBUG", rotation="1 weeks", compression='zip')

app = FastAPI()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check")
    return Message(message="Success")


@app.post("/api/v1/sum", response_model=ResponseCalc, responses={**DEFAULT_RESPONSES})
def calc_sum(sum_request: RequestCalc):
    logger.info("SUM")

    try:
        res = sum_request.number_1 + sum_request.number_2
        return ResponseCalc(res=res)
    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})