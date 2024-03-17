from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn

from controller import Controller
from debug import Debug
from request_data import RequestData


PORT = 8080

webapp = FastAPI()
webapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@webapp.post("/new_data")
async def new_data(data: RequestData):
    timestamp = time.time()
    Debug.process(data, timestamp)
    Controller.process(data, timestamp)

if __name__ == "__main__":
    uvicorn.run(webapp, host="0.0.0.0", port=PORT)
