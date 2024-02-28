from flask import Flask, render_template, request, flash, redirect, url_for
from src.login_autentication import login_autentication
""" import os
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import func
from src.db import db_url  """


app = Flask(__name__)
app.config['SECRET_KEY'] = "senha123"
""" app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False """


# Database config
db = SQLAlchemy(app)

""" class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all() """ 


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