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
    cols = ['id', 'name', 'comment', 'serial', 'date_mod']
#    result = glpi_computers.Computer.query.add_columns('id', 'name', 'comment', 'serial', 'date_mod').slice(((pagenum-1)*numperpage),(pagenum*numperpage))
    result = glpi_computers.Computer.query.with_entities(glpi_computers.Computer.id, glpi_computers.Computer.name, glpi_computers.Computer.comment, glpi_computers.Computer.serial, glpi_computers.Computer.date_mod).all()
    rows = []
    if 'id' in cols:
        for d in result:
            row = {}
            for col in cols:
                row[col] = getattr(d, col)
            rows.append(row)
    else:
        for row in result:
            rows.append(row2dict(row))
#    rows = [d.__dict__ for d in result]
    list['objects'] = rows
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
