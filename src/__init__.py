from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "bd2e9033f993e1cc397db3da55bed60f"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_user.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)