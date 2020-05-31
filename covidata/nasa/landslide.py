import os

import requests
import pandas as pd



class Landslide:
    def __init__(self, subset=-1, verbose=False):
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
            try:
                with open(f'/tmp/landsliade_data.csv', 'w') as data:
                    r = requests.get('https://data.nasa.gov/api/views/dd9e-wu2v/rows.csv?accessType=DOWNLOAD')
                    if verbose:
                        print("Downloaded data")
                    lines = r.text.split('\n')[:subset]
                    for l in lines:
                        l += "\n"
                        data.write(l)
            except:
                os.remove('/tmp/landslide_data.csv')
                raise ConnectionError("You need an internet connection to download the data")
        
        df = pd.read_csv('/tmp/landsliade_data.csv')
        if verbose:
            print("Dataset loaded")
        self.df =  df
    
    def summarize(self):
        return self.df.describe()


if __name__ == '__main__':
    LS = Landslide(subset=100, verbose=True)
    print(LS.summarize())