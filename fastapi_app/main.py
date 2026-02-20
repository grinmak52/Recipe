from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from fastapi_app.core.config import settings
from fastapi_app.api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    uvicorn.run(
        "fastapi_app.main:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
    )
