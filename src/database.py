import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import select, update, insert, delete
from src.products_class import Products, Base
from sqlalchemy_utils import database_exists, create_database
from src.db import db_url


print(db_url)
engine = None
engine = create_engine(db_url)

db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))

Base.query = db_session.query_property()


def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Database created successfully!")
    else:
        print("Database already exists!")
        engine.connect()


def init_tables():
    if sqlalchemy.inspect(engine).has_table("tb_products"):
        print("Table already exists!")
        ret = {"status": "Table already exists!"}
    else:
        import src.products_class
        Base.metadata.create_all(bind=engine)
        print("Table created successfully!")
        ret = {"status": "Table created successfully!"}

    return ret


def insert_product(json_product):
    engine = create_engine(db_url)
    con = engine.connect()

    Session = sessionmaker(engine)
    session = Session()

    query = (
        insert(Products).
        values(
            name        = json_product['name'],
            description = json_product['description'],
            price       = json_product['price'])
    )
    print(query)

    try:
        result = session.execute(query)
        session.commit()
        ret = {"status": "Product has benn added!"}
    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    
    return ret


def update_product(json_product):
    engine = create_engine(db_url)
    con = engine.connect()

    Session = sessionmaker(engine)
    session = Session()

    query = (
        update(Products).
        where(Products.id == json_product['id']).
        values(
            name        = json_product['name'],
            description = json_product['description'],
            price       = json_product['price'])
    )
    print(query)

    try:
        result = session.execute(query)
        session.commit()

        if result.rowcount > 0:
            ret = {"status": "Product has been updated!"}
        else:
            ret = {"status": "Product has not been updated!"}
    except Exception as e:
        print(e)
        ret = {"status": str(e)}

    return ret


def delete_product(json_product):
    engine = create_engine(db_url)
    con = engine.connect()

    Session = sessionmaker(engine)
    session = Session()

    query = (
        delete(Products).
        where(Products.id == json_product['id'])
    )
    print(query)

    try:
        result = session.execute(query)
        session.commit()

        if result.rowcount > 0:
            ret = {"status": "Product has been deleted!"}
        else:
            ret = {"status": "Product did not find!"}
    except Exception as e:
        print(e)
        ret = {"status": str(e)}

    return ret
