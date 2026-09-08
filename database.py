from sqlalchemy import ForeignKey, create_engine, Column, Integer, String,Date, Time, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Crear motor de bases de datos SQLite

engine = create_engine('sqlite:///myDatabase.db' , echo=True)


# Declaracion de la base de datos 

base = declarative_base()

# Crear una clase que representa una tabla

class Product(base):
    __tablename__ = 'products'
    product_Id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

class Sale(base):
    __tablename__ = 'sales'
    sale_Id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    date = Column(Date, nullable=False)
    hour = Column(Time, nullable=False)
    id_product = Column(Integer, ForeignKey('products.product_Id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

# Crear las tablas en la base de datos si no existen

base.metadata.create_all(engine)

# Crear sesion para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

