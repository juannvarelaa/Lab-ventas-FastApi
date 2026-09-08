from fastapi import FastAPI
from database import session, Product, Sale
from schemas import ProductCreate

app = FastAPI()


@app.get("/")
def start():
    return {"message": "Running FastAPI application!"} 


#Agregar un producto a la base de datos por FastAPI
@app.post("/products")
def create_product(product: ProductCreate):


    

    new_product = Product(
        name=product.name,
        price=product.price
    )
    session.add(new_product)
    session.commit()
    session.refresh(new_product)



    return new_product

@app.get("/products")
def get_products():
#Consultar los registros en la base de datos
    products = session.query(Product).all()
    return products