import os

import requests
import pandas as pd


class Gosat:
    def __init__(self, subset=-1, verbose=False, month='02', year='2019'):
        """Loads Data
        # Arguments
            year: a string with the year you want to download the data from 
            month: a string with the month you want to download the data from
            subset: the last row to load in the Dataframe
            verbose
        # Returns
            Dataframe with the data
        """

        if not os.path.exists(f'/tmp/gosat{year}{month}.tsv'):
            if verbose:
                print("Cache not found, downloading data...")
            try:
                with open(f'/tmp/gosat{year}{month}.tsv', 'w') as data:
                    r = requests.get(f'https://www.eorc.jaxa.jp/GOSAT/GPCG/download/data-g2-{year}{month}.txt')
                    if verbose:
                        print("Downloaded data")
                    lines = r.text.split('\n')[11:subset]
                    for l in lines:
                        l = '\t'.join(l.split()) + "\n"
                        data.write(l)
            except:
                os.remove(f'/tmp/gosat{year}{month}.tsv')
                raise ConnectionError("You need an internet connection to download the data")
        
        df = pd.read_csv(f'/tmp/gosat{year}{month}.tsv', '\t')
        if verbose:
            print("Dataset loaded")
        self.df = df
    def summarize(self):
        return self.df.describe()


if __name__ == '__main__':
    GS = Gosat(subset=100, verbose=True)
    print(GS.summarize())