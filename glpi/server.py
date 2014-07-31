#!flask/bin/python
from datetime import timedelta
from flask import Flask, jsonify, abort, request, make_response, url_for, current_app
from functools import update_wrapper
import sys

#import all modules in glpi.objects
from glpi.objects import *


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
	f.required_methods = ['OPTIONS']
        return update_wrapper(wrapped_function, f)
    return decorator


app = Flask(__name__, static_url_path = "")

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/api/v1.0/objects', methods = ['GET'])
@app.route('/api/v1.0/objects/index', methods = ['GET'])
@crossdomain(origin='*')
def get_all_objets():
    return jsonify(  )

@app.route('/api/v1.0/objects/<urlobject>', methods = ['GET'])
@app.route('/api/v1.0/objects/<urlobject>/index', methods = ['GET'])
@app.route('/api/v1.0/objects/<urlobject>/index/<int:pagenum>', methods = ['GET'])
@crossdomain(origin='*')
def get_all(urlobject, pagenum = 1):
    modulename = 'glpi.objects.'+urlobject
    if not modulename in sys.modules:
        return make_response(jsonify( { 'error': 'Not found' } ), 404)
    mymodule = sys.modules[modulename]
    return jsonify( { urlobject: mymodule.getall(pagenum) } )

@app.route('/api/v1.0/objects/<urlobject>/id/<int:id>', methods = ['GET'])
@crossdomain(origin='*')
def get_id(urlobject, id):
    modulename = 'glpi.objects.'+urlobject
    if not modulename in sys.modules:
        return make_response(jsonify( { 'error': 'Not found' } ), 404)
    mymodule = sys.modules[modulename]
    return jsonify( { urlobject: mymodule.getid(id) } )

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

if __name__ == '__main__':
    app.run(debug = True)
