from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import select, update, insert, delete
from src.models import Products, Base
from sqlalchemy_utils import database_exists, create_database
from src.db_url import DB_URL


class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine(DB_URL)

        self.db_session = scoped_session(sessionmaker(autocommit=True,
                                                autoflush=True,
                                                bind=self.engine))

        Base.query = self.db_session.query_property()

        self.init_db()
        self.init_tables()


    def init_db(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            print("Database created successfully!")
        else:
            print("Database already exists!")
            self.engine.connect()


    def init_tables(self):
        if inspect(self.engine).has_table("tb_products"):
            print("Table already exists!")
            ret = {"status": "Table already exists!"}
        else:
            Base.metadata.create_all(bind=self.engine)
            print("Table created successfully!")
            ret = {"status": "Table created successfully!"}

        return ret


    def insert_product(self, json_product):
        Session = sessionmaker(self.engine)
        session = Session()

        query = (
            insert(Products).
            values(
                name        = json_product['name'],
                description = json_product['description'],
                price       = json_product['price'])
        )

        try:
            session.execute(query)
            session.commit()
            ret = {"status": "Product has benn added!"}
        except Exception as e:
            print(e)
            ret = {"status": str(e)}
        
        return ret


    def update_product(self, json_product):
        Session = sessionmaker(self.engine)
        session = Session()

        query = (
            update(Products).
            where(Products.id == json_product['id']).
            values(
                name        = json_product['name'],
                description = json_product['description'],
                price       = json_product['price'])
        )

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


    def delete_product(self, json_product):
        Session = sessionmaker(self.engine)
        session = Session()

        query = (
            delete(Products).
            where(Products.id == json_product['id'])
        )

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


    def select_all_products(self):
        Session = sessionmaker(self.engine)
        session = Session()

        query = select(Products.id, Products.name, Products.description, Products.price)
        products = session.execute(query)

        products_json = []

        for product in products:
            products_json.append(
                {"id": product[0], "name": product[1], "description": product[2], "price": product[3]}
            )
        return products_json