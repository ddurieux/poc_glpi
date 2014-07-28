__author__="ddurieux"
__date__ ="$Jul 26, 2014 11:21:24 AM$"

from math import *

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
    list = {
        'info': 
            {
                'numberelements': len(computers),
                'numberpages': ceil(len(computers)/2)
            }
    }
    list['elements'] = computers
    return list

def getid(id):
    if not id in computers:
        return { 'error': 'Not found' }
    return computers[id]

