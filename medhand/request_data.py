from pydantic import BaseModel


class RequestData(BaseModel):
    x: int
    y: int
    z: int
