from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Liverlona1@34.105.148.169:3306/project_db"


db = SQLAlchemy(app)


from application import routes

