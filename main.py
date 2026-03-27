from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome All"

products=[
    Products(id=1,name="Laptop",description="This is a laptop",price=50000,quantity=10),
    Products(id=2,name="Mobile",description="This is a mobile",price=20000,quantity=20),
    Products(id=3,name="Tablet",description="This is a tablet",price=30000,quantity=15),
    Products(id=4,name="Headphones",description="This is a headphones",price=5000,quantity=30)
]

@app.get("/Products")
def get_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    result=list(filter(lambda x:x.id==id,products))
    if(result):
        return result
    return "Not Found"

@app.post("/product")
def add_product(product:Products):
    products.append(product)
    return product