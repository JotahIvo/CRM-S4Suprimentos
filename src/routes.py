from flask import Flask, render_template, request, flash, redirect, Blueprint
from src.login_autentication import login_autentication
import src.database as database
from src.products_json import products_json


urls_blueprint = Blueprint('urls', __name__)


# Database routes:
@urls_blueprint.route("/init_db", methods=['GET'])
def create_database():
    try:
        database.init_db()
        ret = {"status": "Database are created!"}
    except Exception as e:
        print(e)
        ret = {"status": "Database are not created!"}
    
    return ret


@urls_blueprint.route("/create_tables", methods=['GET'])
def create_tables():
    try:
        database.init_tables()
        ret = {"status": "Tables created successfully!"}
    except Exception as e:
        print(e)
        ret = {"status": "Problems to create tables!"}

    return ret


@urls_blueprint.route("/products", methods=['POST'])
def insert():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']

    products_insert = {"name":name, "description":description, "price":float(price)} 

    database.insert_product(products_insert)
    print(products_insert)

    products = products_json()
    
    return render_template("html/adminPage.html", products=products)


@urls_blueprint.route("/products/update", methods=['POST'])
def update():
    
    id = request.form['id']
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']

    products_update = {"id": id, "name": name, "description": description, "price": price}

    database.update_product(products_update)
    print(products_update)

    products = products_json()
    
    return render_template("html/adminPage.html", products=products)


@urls_blueprint.route("/products/delete", methods=['POST'])
def delete():
    print("entrou")
    id = request.form['id']

    products_delete = {"id": id}

    database.delete_product(products_delete)
    print(products_delete)

    products = products_json()
    
    return render_template("html/adminPage.html", products=products)


# Page routes
@urls_blueprint.route("/") 
def home_page():
    return render_template("html/login.html")


@urls_blueprint.route("/login", methods=['POST']) 
def login():
    products = products_json()

    if request.method == "POST":
        user_input = request.form.get('username')
        password_input = request.form.get('password')
        
        autentication = login_autentication(user_input, password_input)
        if autentication == "/":
            flash('Usuário ou senha inválido(s)')
            return redirect("/")
        else:
            if autentication == "admin":
                return render_template("html/adminPage.html", products=products)
            else:
                return render_template("html/userPage.html", products=products)

        return redirect("/")


@urls_blueprint.route("/logout", methods=['POST']) 
def logout():
    return redirect("/")


@urls_blueprint.route("/create-record", methods=['POST'])
def create_record():
    return render_template("html/createRecord.html")


@urls_blueprint.route("/update-record", methods=['POST'])
def update_button():
    return render_template("html/update.html")