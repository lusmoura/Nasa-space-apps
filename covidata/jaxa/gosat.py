import os

import requests
import pandas as pd



def get(year='2019', month='02', verbose=false):
    """Loads Data
    # Arguments
        year: a string with the year you want to download the data from 
        month: a string with the month you want to download the data from
    # Returns
        Dataframe with the data
    """

    if not os.path.exists('/tmp/gosat.tsv'):
        if verbose:
            print("Cache not found, downloading data...")
        with open(f'/tmp/gosat{year}{month}.tsv', 'w') as data:
            r = requests.get(f'https://www.eorc.jaxa.jp/GOSAT/GPCG/download/data-g2-{year}{month}.txt')
            if verbose:
                print("Downloaded data")
            lines = r.text.split('\n')[11:-1]
            for l in lines:
                l = '\t'.join(l.split()) + "\n"
                data.write(l)
    
    df = pd.read_csv('/tmp/gosat.tsv', '\t')
    if verbose:
        print("Dataset loaded")
    return df


if __name__ == '__main__':
    df = get(verbose=true)
    print(df.head())