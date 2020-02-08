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
import numpy as np

from utils import load_model
from utils import image_decoder


# Global variables
dl_model = '../model/model.json'
dl_weights = '../model/model.h5'
# model <- Call the load_model funtion
labels = [
    'Angry',
    'Disgust',
    'Fear',
    'Happy',
    'Sad',
    'Surprise',
    'Neutral'
]


# API from Flask instance
api = Flask(__name__)


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

    return


def predict_emotion():
    """
    POST method for emotion prediction endpoint.
    """

    # Get data as JSON from POST
    # data <- get_json() from request
    
    # Parse data from JSON
    # raw_img <- 'image' key from data
    
    # Build input vector for DL model
    # input_img <- Call image_decoder() on raw_img
    
    # Predict using DL model
    # prediction <- predict on input_img using the model
    # p_class <- grab the argmax of the prediciton vector
    
    # Serialize predictions for response
    prob_vector = None # TODO
    class_id = None    # TODO
    class_name = None  # TODO
    
    # Send response
    """
    Build message with:
    
    "message": [
            {
                "task": "Facial Emotion Recognition",
                "prob_vector": ???,
                "class_id": ???,
                "class_name": ???
            }
        ]
    """

    return response


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
    # Run API...
    pass