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


def image_encoder(img_path):
    """Function to verify API status.
    
    Parameters
    ----------
    img_path : str
        The path to the image to be encoded.
    
    Returns
    -------
    encoded_img : str
        A string in UTF-8 format containing the encoded image.
    """
    
    with open(img_path, 'rb') as img_file:
        encoded = base64.b64encode(img_file.read())

    encoded_img = encoded.decode('utf-8')

    return encoded_img


def image_decoder(encoded_img):
    """Function to verify API status.
    
    Parameters
    ----------
    encoded_img : str
        The image in base64 (UTF-8) encoded format.
    
    Returns
    -------
    """

    return


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