import os

import requests
import pandas as pd



def get(subset=None, verbose=False):
    """Loads Data
    # Arguments
        subset: the last row to load in the Dataframe
        verbose
    # Returns
        Dataframe with the data
    """

    if not os.path.exists('/tmp/opendata.csv'):
        if verbose:
            print("Cache not found, downloading data...")
        with open(f'/tmp/opendata.csv', 'w') as data:
            r = requests.get(f'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
            if verbose:
                print("Downloaded data")
            lines = r.text.split('\r\n')[:subset]
            for l in lines:
                l += '\n'
                data.write(l)
    
    df = pd.read_csv('/tmp/opendata.csv')
    if verbose:
        print("Dataset loaded")
    return df


if __name__ == '__main__':
    df = get(subset=100, verbose=True)
    print(df.head())