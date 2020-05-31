import os

import requests
import pandas as pd


class OpenData:
    def __init__(self, subset=-1, verbose=False):
        """Loads Data
        # Arguments
            subset: the last row to load in the Dataframe
            verbose
        # Returns
            Dataframe with the data
        """
        super().__init__()
        if not os.path.exists('/tmp/opendata.csv'):
            if verbose:
                print("Cache not found, downloading data...")
            try:
                with open(f'/tmp/opendata.csv', 'w') as data:
                    r = requests.get(f'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
                    if verbose:
                        print("Downloaded data")
                    lines = r.text.split('\r\n')[:subset]
                    for l in lines:
                        l += '\n'
                        data.write(l)
            except:
                os.remove('/tmp/opendata.csv')
                raise ConnectionError("You need an internet connection to download the data")
        
        df = pd.read_csv('/tmp/opendata.csv')
        if verbose:
            print("Dataset loaded")
        self.df = df
    def summarize(self):
        return self.df.describe()


if __name__ == '__main__':
    OD = OpenData(subset=100, verbose=True)
    print(OD.summarize())