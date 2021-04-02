from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
