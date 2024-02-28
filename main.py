from flask import Flask, render_template, request, flash, redirect
from src.login_autentication import login_autentication


app = Flask(__name__)
app.config['SECRET_KEY'] = "senha123"


@app.route("/")
def home_page():
    return render_template("html/login.html")


@app.route("/login", methods=['POST'])
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


@app.route("/logout", methods=['POST'])
def logout():
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)