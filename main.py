from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

PORT = 8080

# init website

webapp = FastAPI()
webapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Position(BaseModel):
    x: int
    y: int
    z: int

# routes

@webapp.post("/position")
async def set_position(data: Position):
    x, y, z = data.x, data.y, data.z
    print(f"Received position values - x: {x}, y: {y}, z: {z}")
    return {"x": x, "y": y, "z": z}

# run

def serve():
    uvicorn.run(webapp, port=PORT)

if __name__ == "__main__":
    serve()