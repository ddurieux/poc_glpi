from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('glpi.config')
db = SQLAlchemy(app)

from glpi.database import *
