from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Liverlona1@34.105.145.252:3306/project_db"
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))


db = SQLAlchemy(app)


from application import routes

