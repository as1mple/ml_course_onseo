from pydantic import BaseModel


class Message(BaseModel):
    message: str


class RequestCalc(BaseModel):
    number_1: float
    number_2: float


class ResponseCalc(BaseModel):
    res: float
