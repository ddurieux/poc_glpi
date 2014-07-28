#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import sys

#import all modules in glpi.objects
from glpi.objects import *

app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/api/v1.0/objects/<urlobject>', methods = ['GET'])
@app.route('/api/v1.0/objects/<urlobject>/index', methods = ['GET'])
@app.route('/api/v1.0/objects/<urlobject>/index/<pagenum>', methods = ['GET'])
def get_all(urlobject, pagenum = 0):
    modulename = 'glpi.objects.'+urlobject
    if not modulename in sys.modules:
        return make_response(jsonify( { 'error': 'Not found' } ), 404)
    mymodule = sys.modules[modulename]
    return jsonify( { urlobject: mymodule.getall() } )

@app.route('/api/v1.0/objects/<urlobject>/id/<int:id>', methods = ['GET'])
def get_id(urlobject, id):
    if (module_exists(urlobject)):
        i = __import__(urlobject)
        return jsonify( { 'computers': i.getid(id) } )


def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

if __name__ == '__main__':
    app.run(debug = True)
