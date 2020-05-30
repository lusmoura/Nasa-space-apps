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

    if not os.path.exists('/tmp/mortality_natality.tsv'):
        if verbose:
            print("Cache not found, downloading data...")
        with open(f'/tmp/mortality_natality.tsv', 'w') as data:
            r = requests.get('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/urb_lfermor.tsv.gz&unzip=true')
            if verbose:
                print("Downloaded data")
            lines = r.text.split('\n')[:subset]
            for l in lines:
                l += "\n"
                data.write(l)
    
    df = pd.read_csv('/tmp/mortality_natality.tsv', '\t')
    if verbose:
        print("Dataset loaded")
    return df


if __name__ == '__main__':
    df = get(subset=100, verbose=True)
    print(df.head())