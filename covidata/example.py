import request
import pandas as pd

def get(path=''):
    """Loads Data
    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.keras/datasets).
    # Returns
        Dataframe or numpy arrays (if image)
    """
    data = request.get(
        path,
        origin='https://s3.amazonaws.com/keras-datasets/boston_housing.npz')
    df = pandas.read_csv(data)
    
    return df