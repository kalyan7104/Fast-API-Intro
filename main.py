from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome All"

products=[
    Products(1,"Asus Laptop","Laptop",1000,5),
    Products(2,"Dell Laptop","Laptop",100,1)
]

@app.get("/Products")
def get_products():
    return products

