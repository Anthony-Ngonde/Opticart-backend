from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.order import Glass, Order
from db import cursor, conn

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"])


class OrderModel(BaseModel):
    name: str
    email: str
    address: str
    item_purchased: str
    total_price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/glasses')
def glasses():
    glasses = Glass.find_all()
    return glasses

@app.post('/order')
def save_order(order_data: OrderModel):
    order = Order(
        name=order_data.name,
        email=order_data.email,
        address=order_data.address,
        item_purchased=order_data.item_purchased,
        total_price=order_data.total_price
    )
    order.save()
    return {"message": "Order saved successfully"}

@app.get('/orders')
def get_orders():
    sql = "SELECT * FROM orders"
    rows = cursor.execute(sql).fetchall()
    orders = [
        {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "address": row[3],
            "item_purchased": row[4],
            "total_price": row[5],
        }
        for row in rows
    ]
    return orders

@app.delete('/order/{order_id}')
def delete_order(order_id: int):
    sql = "DELETE FROM orders WHERE id = ?"
    cursor.execute(sql, (order_id,))
    conn.commit()
    return {"message": "Order deleted successfully"}