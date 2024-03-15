import debug

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from controller import Controller
from position import Position


PORT = 8080

webapp = FastAPI()
webapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@webapp.post("/position")
async def set_position(data: Position):
    Controller.process(data)

if __name__ == "__main__":
    uvicorn.run(webapp, host="0.0.0.0", port=PORT)
