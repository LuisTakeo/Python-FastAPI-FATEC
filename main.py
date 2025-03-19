from typing import Union
from fastapi import FastAPI
from routes.router import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.22.1", port=8000)