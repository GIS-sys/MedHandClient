from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Position(BaseModel):
    x: int
    y: int
    z: int

@app.post("/position")
async def set_position(data: Position):
    x, y, z = data.x, data.y, data.z
    print(f"Received position values - x: {x}, y: {y}, z: {z}")
    return {"x": x, "y": y, "z": z}
