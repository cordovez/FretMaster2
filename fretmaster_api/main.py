from fastapi import FastAPI
from contextlib import asynccontextmanager
from mongodb.connect_db import init_db
from mongodb.queries import insert

db = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global db
    db = await init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/add")
async def add():
    document = {"test_key2": "test_value2"}
    return await insert(document, db)
