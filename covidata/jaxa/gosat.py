import os

import requests
import pandas as pd



def get(path=''):
    """Loads Data
    # Arguments
        path: path where to cache the dataset locally
    # Returns
        Dataframe or numpy arrays (if image)
    """

    if not os.path.exists('/tmp/gosat.tsv'):
        with open('/tmp/gosat.tsv', 'w') as data:
            r = requests.get('https://www.eorc.jaxa.jp/GOSAT/GPCG/download/data-g2-201902.txt')
            lines = r.text.split('\n')[11:-1]
            for l in lines:
                l = '\t'.join(l.split()) + "\n"
                data.write(l)
    
    df = pd.read_csv('/tmp/gosat.tsv', '\t')
    
    return df


if __name__ == '__main__':
    df = get()
    print(df.head())