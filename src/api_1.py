from fastapi import FastAPI
from fastapi.responses import JSONResponse
from loguru import logger

from .modules.data_models import Message
from .modules.data_models import RequestHouseParams, ResponsePrice
from .modules.simple_ml_models import HousePriceModel

DEFAULT_RESPONSES = {500: {'model': Message}}

logger.add('deb  ug.log', format="{time} {level} {message}", level="DEBUG", rotation="1 weeks", compression='zip')

app = FastAPI()
app.model = HousePriceModel()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check")
    return Message(message="Success")


@app.post("/api/v1/house_price", response_model=ResponsePrice, responses={**DEFAULT_RESPONSES})
def calc_sum(house_params: RequestHouseParams):
    logger.info("house_price")

    try:

        price = app.model(area=house_params.area,
                          n_floors=house_params.n_floors,
                          heating=house_params.heating)
        return ResponsePrice(price=price)

    except Exception as e:
        logger.exception(str(e))
        return JSONResponse(status_code=500, content={'message': str(e)})
