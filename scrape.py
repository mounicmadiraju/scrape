# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:07:19 2017

@author: mounic
"""
import requests
from bs4 import BeautifulSoup
import json
URL = "https://www.numbeo.com/cost-of-living/"

class Extract_table:
    """ Extracts the table from the beautiful soup html page"""
    def __init__(self, page):
        self.Data = {}
        self.Table = page.find("table", {'class':'data_wide_table'}) #finding table with class name
    def extract(self):
        """A method to extract the table contents and store to a dict"""
        if not self.Table:
            return None #check if it is in the format.
        for row in self.Table("tr"):
            if row("th"):
                key = row("th")[0].text
                self.Data[key] = []
            else:
                self.Data[key].append([cell.text for cell in row("td")])
        return self.Data

if __name__ == "__main__":
    COUNTRY = ['Malaysia']
    results = {} 
    