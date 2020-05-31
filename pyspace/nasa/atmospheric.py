import os

import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
from .earthdata_login import login_data, headers


class Atmospheric:
    """Contains the NASA Atmospheric data
       Atributes
       ---------
       df: pandas.DataFrame
            Dataframe with atmospheric data

       Methods
       -------
        summarize
            Returns summary statistics of the dataset
    """
    
    def __init__(self, username, password, subset=-1, verbose=False):
        """Instantiates the object and downloads the data
        # Arguments
            subset: the last row to load in the Dataframe
            verbose
        # Returns
            Dataframe with the data
        """

        if not os.path.exists('/tmp/atmosferic_gas_concentration.csv'):
            if verbose:
                print("Cache not found, downloading data...")
            try:
                with open('/tmp/atmosferic_gas_concentration.csv', 'w') as data:
                    with requests.Session() as s:
                        login_url = 'https://urs.earthdata.nasa.gov/oauth/authorize?client_id=YQOhivHfMTau88rjbMOVyg&response_type=code&redirect_uri=https://daac.ornl.gov/cgi-bin/urs/urs_logon_proc.pl&state=https%3A%2F%2Fdaac.ornl.gov%2F'
                        download_url = 'https://daac.ornl.gov/daacdata/above/ABoVE_Atmospheric_Flask_Data/data/ABoVE_april-nov_2017_flask_data.csv'
                        
                        r = s.get(login_url, headers=headers)
                        html = soup(r.content, "lxml")

                        auth = html.find("input", attrs={'name':'authenticity_token'})['value']
                        login_data['authenticity_token'] = auth
                        login_data['username'] = username
                        login_data['password'] = password

                        s.post('https://urs.earthdata.nasa.gov/login', data=login_data, headers=headers)
                        r = s.get(download_url, headers=headers)
            
                    if verbose:
                        print("Downloaded data")
                    lines = r.text.split('\n')[:subset]
                    for l in lines:
                        l += "\n"
                        data.write(l)
            except:
                os.remove('atmosferic_gas_concentration.csv')
                raise ConnectionError("You need an internet connection to download the data")
    
        df = pd.read_csv('/tmp/atmosferic_gas_concentration.csv')
        if verbose:
            print("Dataset loaded")
        self.df = df
    
    def summarize(self):
        """Returns summary statistics of the dataset"""
        return self.df.describe()

if __name__ == '__main__':
    AG = Atmospheric(subset=100, verbose=True, username='username', password='password')
    print(AG.summarize())