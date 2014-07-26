#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
import sys
sys.path.append('objects')
import computers

app = Flask(__name__, static_url_path = "")
 
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
 
@app.route('/api/v1.0/computers', methods = ['GET'])
def get_all_computers():
    return jsonify( { 'computers': computers.get_computers() } )

if __name__ == '__main__':
    app.run(debug = True)