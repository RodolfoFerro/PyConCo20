# ==============================================================
# Author: Rodoflo Ferro
# Email: ferro@cimat.mx
# Twitter: @rodo_ferro
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro,
# for his workshop at PyCon Colombia 2020. Any explicit usage
# of this script or its contents is granted according to
# the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

from utils import image_encoder
from utils import image_decoder
from utils import save_output

import requests


def check_status(url, verbose=True, outfile=False):
    """Function to verify the API status.
    
    Parameters
    ----------
    url : str
        The endpoint to verify the API status.
    verbose : bool
        A flag to print the text output.
    outfile : bool
        A flag to save the text output into a JSON file.
    
    Returns
    -------
    response : dict
        The response as a JSON object.
    """
    
    r = requests.get(url)
    response = r.json()
    
    if outfile:
        save_output(r.text, 'check_status.json')
    
    if verbose:
        print(r.text)

    return response


def predict_emotion(img_path, url, verbose=True, outfile=False):
    """Function to call the emotion predictor API.
    
    Parameters
    ----------
    img_path : str
        The path to the image to be processed.
    url : str
        The endpoint to verify the API status.
    verbose : bool
        A flag to print the text output.
    outfile : bool
        A flag to save the text output into a JSON file.
    
    Returns
    -------
    response : dict
        The response as a JSON object.
    """
    
    encoded_img = image_encoder(img_path)

    data = {
        "image": encoded_img
    }
    
    r = requests.post(url, json=data)
    response = r.json()
    
    if outfile:
        save_output(r.text, 'predict_emotion.json')
    
    if verbose:
        print(r.text)

    return response
    

if __name__ == '__main__':
    # Test API on status route
    print('=== API status check ===')
    r = check_status('http://localhost:5000/api/status')
    
    # Predict emotion form image
    print('=== API emotion classification ===')
    p = predict_emotion('../media/Happy.png', 'http://localhost:5000/api/emotion')

