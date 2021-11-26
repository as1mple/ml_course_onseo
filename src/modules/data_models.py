from pydantic import BaseModel


class Message(BaseModel):
    message: str


class RequestCalc(BaseModel):
    number_1: float
    number_2: float


class ResponseCalc(BaseModel):
    res: float


class RequestHouseParams(BaseModel):
    area: float = 50
    n_floors: int = 3
    heating: str = "A"


class ResponsePrice(BaseModel):
    price: float


class RequestText(BaseModel):
    text: str = "Good idea"


class ResponseSentiment(BaseModel):
    sentiment: int
    score: int
