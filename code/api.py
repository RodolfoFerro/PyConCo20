# ==============================================================
# Author: Rodoflo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro,
# for his workshop at PyCon Colombia 2020. Any explicit usage
# of this script or its contents is granted according to
# the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify


api = Flask(__name__)


@api.route('/api/status', methods=['GET'])
def status():
    """
    GET method for API status verification.
    """
    
    message = {
        "status": 200,
        "message": [
            "This API is up and running!"
        ]
    }
    response = jsonify(message)
    response.status_code = 200

    return response


@api.route('/api/emotion', methods=['POST'])
def predict_emotion():
    """
    POST method for emotion prediction endpoint.
    """

    # Get data as JSON from POST
    data = request.get_json()
    
    # Parse data from JSON
    
    # Build input vector for DL model
    input_vec = None
    
    # Predict using DL model
    
    return


@api.errorhandler(404)
def not_found(error=None):
    """
    GET method for not found routes.
    """
    
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