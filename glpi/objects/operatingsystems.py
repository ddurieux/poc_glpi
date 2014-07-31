__author__="ddurieux"
__date__ ="$Jul 26, 2014 11:21:24 AM$"

from math import *
from glpi import db
from glpi.database import *

def getall(pagenum):
    # test pagination 2 per pages
    num_rows = glpi_operatingsystems.OperatingSystem.query.count()
    list = {
        'num_results': num_rows,
        'total_pages': ceil(num_rows/2),
        'page': pagenum
    }
    result = glpi_operatingsystems.OperatingSystem.query.slice(((pagenum-1)*2),(pagenum*2))
    rows = []
    for row in result:
        rows.append(row2dict(row))
    list['objects'] = rows
    return list

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d
