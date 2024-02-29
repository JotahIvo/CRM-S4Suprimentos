from flask import Flask, render_template, request, flash, redirect, url_for
from src.login_autentication import login_autentication
import os
#from flask_sqlalchemy import SQLAlchemy 
#from sqlalchemy.sql import func
import src.database as database
from src.db import db_url  


app = Flask(__name__)
app.config['SECRET_KEY'] = "senha123"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Database routes:
@app.route("/init_db", methods=['GET'])
def create_database():
    try:
        database.init_db()
        ret = {"status": "Database are created!"}
    except Exception as e:
        print(e)
        ret = {"status": "Database are not created!"}
    
    return ret


@app.route("/create_tables", methods=['GET'])
def create_tables():
    try:
        database.init_tables()
        ret = {"status": "Tables created successfully!"}
    except Exception as e:
        print(e)
        ret = {"status": "Problems to create tables!"}

    return ret


@app.route("/insert_products", methods=['POST'])
def insert():
    req_data = request.get_json()
    products_json = {"name": req_data['name'], "description": req_data['description'], "price": req_data['price']}

    ret = database.insert_product(products_json)
    print(products_json)
    
    return ret


@app.route("/update_products", methods=['PUT'])
def update():
    req_data = request.get_json()
    products_json = {"id": req_data['id'], "name": req_data['name'], "description": req_data['description'], "price": req_data['price']}

    ret = database.update_product(products_json)
    print(products_json)

    return ret


@app.route("/delete_products", methods=['DELETE'])
def delete():
    req_data = request.get_json()
    products_json = {"id": req_data['id']}

    ret = database.delete_product(products_json)
    print(products_json)

    return ret


# Page routes
@app.route("/") #home
def home_page():
    return render_template("html/login.html")


@app.route("/login", methods=['POST']) #login
def login():
    user_input = request.form.get('username')
    password_input = request.form.get('password')
    
    autentication = login_autentication(user_input, password_input)
    if autentication == "/":
        flash('Usuário ou senha inválido(s)')
        return redirect("/")
    else:
        if autentication == "admin":
            return render_template("html/adminPage.html", username='Administrador')
        else:
            return render_template("html/userPage.html", username='Usuário')

    return redirect("/")


@app.route("/logout", methods=['POST']) #logout
def logout():
    return redirect("/")


@app.route("/create-record", methods=['POST'])
def create_record():
    return render_template("html/createRecord.html")


if __name__ == '__main__':
    app.run(debug=True)