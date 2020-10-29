from fastapi import FastAPI

from app.core import config
app = FastAPI(
    title=config.PROJECT_NAME,
    description="",
    version="0.1",
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)

