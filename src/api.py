"""
http://127.0.0.1:18000/api/data?input=xxx
"""

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from copy import copy

class Api:
    def __init__(self):
        self.res = {'success': True, 'data': None}

    def process(self, request_args):
        res = copy(self.res)
        res['data'] = request_args.get('input', 'Default input value')
        return res

app = Flask(__name__)
CORS(app, origins=['http://localhost:8080', 'https://api.qtumx.info'])
api = Api()

@app.route('/api/data')
def api_data():
    res = api.process(request.args)
    return jsonify(res)

if __name__ == "__main__":
    app.run()