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

import base64
from io import BytesIO

import numpy as np
from PIL import Image


def image_encoder(img_path):
    """Function to verify API status.
    
    Parameters
    ----------
    img_path : str
        The path to the image to be encoded.
    
    Returns
    -------
    encoded_img : str
        A bytes string containing the encoded image.
    """
    
    with open(img_path, 'rb') as img_file:
        encoded_img = base64.b64encode(img_file.read())

    return encoded_img


def image_decoder(encoded_img):
    """Function to verify API status.
    
    Parameters
    ----------
    encoded_img : str
        The image in base64 (UTF-8) encoded format.
    
    Returns
    -------
    img : ndarray
        The decoded image as a NumPy array.
    """

    decoded_img = base64.decodebytes(encoded_img)
    img = Image.open(BytesIO(decoded_img))
    img = np.asarray(img)

    return img


def save_output(text, filename):
    """Function to save API output.
    
    Parameters
    ----------
    text : str
        The etxt to be saved into the output file.
    filename : str
        The name of the output file.
    """

    with open(filename, 'wt') as outfile:
        outfile.write(text)

    return