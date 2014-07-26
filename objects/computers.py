__author__="ddurieux"
__date__ ="$Jul 26, 2014 11:21:24 AM$"


computers = [
    {
    },
    {
        'id': 1,
        'name': u'pc001',
        'serial': u'jth52745n'
    },
    {
        'id': 2,
        'name': u'miranda',
        'serial': u'' 
    }
]

def getall():
    return computers

def getid(id):
    return computers[id]

