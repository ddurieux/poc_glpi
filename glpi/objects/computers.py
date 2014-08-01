__author__="ddurieux"
__date__ ="$Jul 26, 2014 11:21:24 AM$"

from math import *
from glpi import db
from glpi.database import *

def getall(pagenum):
    numperpage = 100000
    # test pagination 2 per pages
    num_rows = glpi_computers.Computer.query.count()
    list = {
        'num_results': num_rows,
        'total_pages': ceil(num_rows/numperpage),
        'page': pagenum
    }
    list['objects'] = glpi_computers.Computer.query.with_entities(glpi_computers.Computer.id, glpi_computers.Computer.name, glpi_computers.Computer.comment, glpi_computers.Computer.serial, glpi_computers.Computer.date_mod).slice(((pagenum-1)*numperpage),(pagenum*numperpage)).all()
    return list

def getid(id):
    if not id in computers:
        return { 'error': 'Not found' }
    return computers[id]

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))
    return d
