from fastapi import FastAPI
from pydantic import BaseModel
from models.order import Glass

app = FastAPI()

class OrderModel(BaseModel):
    name: str
    email: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/glasses')
def glasses():
    glasses = Glass.find_all()
    return glasses

@app.get('/order')
def get_orders():
    return [{"name": "Inferno"}]

@app.post('/order')
def save_orders(data: OrderModel):
    print(data)