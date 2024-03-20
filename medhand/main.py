from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn

import config
from controller import Controller
from debug import Debug
from request_data import RequestData


PORT = config.MAIN_PORT

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
    return "new"

@webapp.get("/{ax}/{ay}/{az}/{gx}/{gy}/{gz}")
async def new_data(ax: float, ay: float, az: float, gx: float, gy: float, gz: float):
    timestamp = time.time()
    data = RequestData(ax=ax, ay=ay, az=az, gx=gx, gy=gy, gz=gz)
    Debug.process(data, timestamp)
    Controller.process(data, timestamp)
    return "new"

if __name__ == "__main__":
    uvicorn.run(webapp, host="0.0.0.0", port=PORT)
