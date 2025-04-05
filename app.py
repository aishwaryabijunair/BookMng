import uvicorn
from fastapi import FastAPI

from scripts.configurations import configurations
from scripts.services.services import router

lib_app = FastAPI()

lib_app.include_router(router)



if __name__ == "__main__" :
    uvicorn.run(lib_app, host = configurations.Service.host,
        port = int(configurations.Service.port))
