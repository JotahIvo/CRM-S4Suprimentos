from flask import Flask, render_template, request, flash, redirect, Blueprint
from src.login_autentication import login_autentication
from src.database import DatabaseConnection


urls_blueprint = Blueprint('urls', __name__)

database = DatabaseConnection()


@urls_blueprint.route("/products/insert", methods=['POST'])
def insert():
    products_insert = {
        "name": request.form['name'], 
        "description": request.form['description'], 
        "price": float(request.form['price'])
    } 

    database.insert_product(products_insert)
    
    return redirect("/admin")


@urls_blueprint.route("/products/update", methods=['POST'])
def update():
    products_update = {
        "id": request.form['id'], 
        "name": request.form['name'], 
        "description": request.form['description'], 
        "price": float(request.form['price'])
    }

    database.update_product(products_update)

    return redirect("/admin")


@urls_blueprint.route("/products/delete", methods=['POST'])
def delete():
    products_delete = {
        "id": request.form['id']
    }

    database.delete_product(products_delete)
    
    return redirect("/admin")


@urls_blueprint.route("/") 
def home_page():
    return render_template("html/login.html")


@urls_blueprint.route("/login", methods=['POST']) 
def login():
    user_input = request.form.get('username')
    password_input = request.form.get('password')
    
    autentication = login_autentication(user_input, password_input)
    if autentication == "/":
        flash('Usuário ou senha inválido(s)')
        return redirect("/")
    else:
        if autentication == "admin":
            return redirect("/admin")
        else:
            return redirect("/user")


@urls_blueprint.route("/logout", methods=['POST']) 
def logout():
    return redirect("/")


@urls_blueprint.route("/products/create-record", methods=['POST'])
def create_record():
    return render_template("html/createRecord.html")


@urls_blueprint.route("/products/update-record", methods=['POST'])
def update_button():
    return render_template("html/update.html")


@urls_blueprint.route("/admin")
def admin_page():
    products = database.select_all_products()
    return render_template("html/adminPage.html", products=products)


@urls_blueprint.route("/user")
def user_page():
    products = database.select_all_products()
    return render_template("html/userPage.html", products=products)


@urls_blueprint.route("/back", methods=['POST'])
def back():
    return redirect("/admin")