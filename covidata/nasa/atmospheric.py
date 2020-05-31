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

    if not os.path.exists('/tmp/atmosferic_gas_concentration.csv'):
        if verbose:
            print("Cache not found, downloading data...")
        with open(f'/tmp/atmosferic_gas_concentration.csv', 'w') as data:
            r = requests.get('https://daac.ornl.gov/daacdata/above/ABoVE_Atmospheric_Flask_Data/data/ABoVE_april-nov_2017_flask_data.csv')
            if verbose:
                print("Downloaded data")
            lines = r.text.split('\n')[:subset]
            for l in lines:
                l += "\n"
                data.write(l)
    
    df = pd.read_csv('/tmp/atmosferic_gas_concentration.csv', '\t')
    if verbose:
        print("Dataset loaded")
    return df


if __name__ == '__main__':
    df = get(subset=100, verbose=True)
    print(df.head())