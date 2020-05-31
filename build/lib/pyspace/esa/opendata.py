import os

import requests
import pandas as pd


class OpenData:
    """Contains the EU open data Covid case distribution
       Atributes
       ---------
       df: pandas.DataFrame
            Dataframe with Covid-19 case distribution

       Methods
       -------
        summarize
            Returns summary statistics of the dataset
    """

    def __init__(self, subset=-1, verbose=False):
        """Instantiates the object and downloads the data
        # Arguments
            subset: the last row to load in the Dataframe
            verbose
        # Returns
            Dataframe with the data
        """
        
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
        """Returns summary statistics of the dataset"""
        return self.df.describe()


if __name__ == '__main__':
    OD = OpenData(subset=100, verbose=True)
    print(OD.summarize())