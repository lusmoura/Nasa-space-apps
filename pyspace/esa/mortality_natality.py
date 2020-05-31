import os

import requests
import pandas as pd


class MortalityNatality:
    """Contains the ESA Mortality and Natality Data
       Atributes
       ---------
       df: pandas.DataFrame
            Dataframe with mortality and natality data

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
        
        if not os.path.exists('/tmp/mortality_natality.tsv'):
            if verbose:
                print("Cache not found, downloading data...")
            try:
                with open('/tmp/mortality_natality.tsv', 'w') as data:
                    r = requests.get('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/urb_lfermor.tsv.gz&unzip=true')
                    if verbose:
                        print("Downloaded data")
                    lines = r.text.split('\n')[:subset]
                    for l in lines:
                        l += "\n"
                        data.write(l)
            except:
                os.remove('/tmp/mortality_natality.tsv')
                raise ConnectionError("You need an internet connection to download the data")
                
    
        df = pd.read_csv('/tmp/mortality_natality.tsv', '\t')
        if verbose:
            print("Dataset loaded")
        self.df = df

    def summarize(self):
        """Returns summary statistics of the dataset"""
        return self.df.describe()
    


if __name__ == '__main__':
    MN = MortalityNatality(subset=100, verbose=True)
    print(MN.summarize())