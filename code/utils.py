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

from io import BytesIO
import base64

import numpy as np
from PIL import Image
from tensorflow import keras


def image_encoder(img_path):
    """Function to verify API status.
    
    Parameters
    ----------
    img_path : str
        The path to the image to be encoded.
    
    Returns
    -------
    encoded_img : str
        A UTF-8 string containing the encoded image.
    """
    
    with open(img_path, 'rb') as img_file:
        encoded_img = base64.b64encode(img_file.read())

    return encoded_img.decode('utf-8')


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

    decoded_img = base64.b64decode(encoded_img)
    data_bytes_io = BytesIO(decoded_img)
    img = Image.open(data_bytes_io)
    img = np.asarray(img)
    
    # We need to extend one dimension for DL model input
    img = img[:,:,0].reshape(1, 48, 48, 1).astype('float32')

    return img


def save_output(text, filename):
    """Function to save API output.
    
    Parameters
    ----------
    text : str
        The text to be saved into the output file.
    filename : str
        The name of the output file.
    """

    with open(filename, 'wt') as outfile:
        outfile.write(text)

    return


def load_model(architecture, weights):
    """Function to load a trained model.
    
    Parameters
    ----------
    architecture : str
        The JSON file containing the architecture of the model.
    weights : str
        The H5 file containing the trained weights of the model.
    
    Returns
    -------
    model : model-like
        A trained and complied TF 2.0 model ready to be used.
    """
    
    # Load model architecture
    json_file = open(architecture, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = keras.models.model_from_json(loaded_model_json)

    # Load weights into loaded model
    model.load_weights(weights)
    print("[INFO] Loaded model from disk.")

    # Compile model
    loss, optimizer, metrics = 'categorical_crossentropy', 'sgd', ['accuracy']
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
    print("[INFO] Compiled model.")

    return model
