from fastapi import FastAPI
from app.routers import translate

app = FastAPI()


app.include_router(translate.router)