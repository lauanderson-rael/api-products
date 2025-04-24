from fastapi import FastAPI
from product import Product
from json_db import JsonDB

app = FastAPI()

productDb = JsonDB(path="./data/products.json")

@app.get("/products")
def get_products():
   products = productDb.read()
   return {"products": products}


@app.post("/products")
def create_products(product: Product):
   productDb.insert(product)
   return {"status": "Inserted"}
