import os

import requests
import pandas as pd



def get(subset=-1, verbose=False):
    """Loads Data
    # Arguments
        subset: the last row to load in the Dataframe
        verbose
    # Returns
        Dataframe with the data
    """

    if not os.path.exists('/tmp/landsliade_data.csv'):
        if verbose:
            print("Cache not found, downloading data...")
        with open(f'/tmp/landsliade_data.csv', 'w') as data:
            r = requests.get('https://data.nasa.gov/api/views/dd9e-wu2v/rows.csv?accessType=DOWNLOAD')
            if verbose:
                print("Downloaded data")
            lines = r.text.split('\n')[:subset]
            for l in lines:
                l += "\n"
                data.write(l)
    
    df = pd.read_csv('/tmp/landsliade_data.csv')
    if verbose:
        print("Dataset loaded")
    return df


if __name__ == '__main__':
    df = get(subset=100, verbose=True)
    print(df.head())