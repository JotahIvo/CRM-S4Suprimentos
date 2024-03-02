from flask import Flask, render_template, request, flash, redirect, url_for
from src.login_autentication import login_autentication
import src.database as database
from src.db import db_url  
from src.products_json import products_json


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


@app.route("/products", methods=['POST'])
def insert():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']

    products_insert = {"name":name, "description":description, "price":float(price)} 

    database.insert_product(products_insert)
    print(products_insert)
    
    products = products_json()
    
    return render_template("html/adminPage.html", products=products)


@app.route("/products/update", methods=['POST'])
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


@app.route("/products/delete", methods=['POST'])
def delete():
    print("entrou")
    id = request.form['id']

    products_delete = {"id": id}

    database.delete_product(products_delete)
    print(products_delete)

    products = products_json()
    
    return render_template("html/adminPage.html", products=products)


# Page routes
@app.route("/") #home
def home_page():
    return render_template("html/login.html")


@app.route("/login", methods=['POST']) #login
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


@app.route("/logout", methods=['POST']) #logout
def logout():
    return redirect("/")


@app.route("/create-record", methods=['POST'])
def create_record():
    return render_template("html/createRecord.html")


@app.route("/update-record", methods=['POST'])
def update_button():
    return render_template("html/update.html")                                                                                                                                                                                                                                              


if __name__ == '__main__':
    app.run(debug=True)