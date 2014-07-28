#!flask/bin/python
from migrate.versioning import api
from glpi.config import SQLALCHEMY_DATABASE_URI
from glpi import db
import os.path
db.create_all()
if not os.path.exists('glpi.database'):
    api.create('glpi.database', 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, 'glpi.database')
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, 'glpi.database', api.version('glpi.database'))
