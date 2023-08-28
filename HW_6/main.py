from data_base import *
from fastapi import FastAPI
import orders
import users
import products

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(users.router, tags=['users'])
app.include_router(products.router, tags=['products'])
app.include_router(orders.router, tags=['orders'])