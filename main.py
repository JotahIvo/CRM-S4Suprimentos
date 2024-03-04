from flask import Flask
from src.db_url import DB_URL  
from src.routes import urls_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = "senha123"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(urls_blueprint)                                                                                                                                                                                                                                              


if __name__ == '__main__':
    app.run(debug=True)