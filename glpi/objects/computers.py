__author__="ddurieux"
__date__ ="$Jul 26, 2014 11:21:24 AM$"

from math import *
from glpi import db
from glpi.database import glpi_computers

computers = {
    1: {
        'id': 1,
        'name': u'pc001',
        'serial': u'jth52745n'
    },
    2: {
        'id': 2,
        'name': u'miranda',
        'serial': u'' 
    },
    3: {
        'id': 3,
        'name': u'pc00x',
        'serial': u'crhn53bvf5'
    }
}

def getall(pagenum):
    # test pagination 2 per pages
    num_rows = glpi_computers.Computer.query.count()
    list = {
        'num_results': num_rows,
        'total_pages': ceil(num_rows/2),
        'page': pagenum
    }
    result = glpi_computers.Computer.query.slice(((pagenum-1)*2),(pagenum*2))
    rows = []
    for row in result:
        rows.append(row2dict(row))
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
