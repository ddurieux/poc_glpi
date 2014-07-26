#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import sys
sys.path.append('objects')

app = Flask(__name__, static_url_path = "")
 
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
 
@app.route('/api/v1.0/objects/<urlobject>', methods = ['GET'])
def get_all(urlobject):
    if (module_exists(urlobject)):
        i = __import__(urlobject)
        return jsonify( { 'computers': i.getall() } )

@app.route('/api/v1.0/objects/<urlobject>/<int:id>', methods = ['GET'])
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