from flask import Flask
from flask import request
from flask import jsonify


api = Flask(__name__)


@api.route('/api/status', methods=['GET'])
def status():
    """Function for the status route."""
    
    message = {
        "status": 200,
        "message": [
            "This API is up and running!"
        ]
    }
    response = jsonify(message)
    response.status_code = 200

    return response


@api.errorhandler(404)
def not_found(error=None):
    """Function for not found routes."""
    
    message = {
        "status": 404,
        "message": [
            "[ERROR] URL not found."
        ]
    }
    response = jsonify(message)
    response.status_code = 404
    
    return response


if __name__ == '__main__':
    api.run(port=5000, debug=True)