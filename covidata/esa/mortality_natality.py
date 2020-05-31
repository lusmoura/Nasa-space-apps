import os

import requests
import pandas as pd


class MortalityNatality:
    def __init__(self, subset=-1, verbose=False):
        """Loads Data
        # Arguments
            subset: the last row to load in the Dataframe
            verbose
        # Returns
            Dataframe with the data
        """
        super().__init__()
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
        self.df = df

    def summarize(self):
        return self.df.describe()
    


if __name__ == '__main__':
    MN = MortalityNatality(subset=100, verbose=True)
    print(MN.summarize())