from pydantic import BaseModel


class RequestData(BaseModel):
    ax: float
    ay: float
    az: float
