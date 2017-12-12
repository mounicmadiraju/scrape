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

class API(object):
    """API to get a country"""
    def __init__(self, BASE_URL, Country, city=0):
        self.base = BASE_URL
        self.url = BASE_URL+"country_result.jsp?country="+Country
        self.country = Country
        self.result = {}
        responce = self.get_page(self.url)
        if responce:
            self.page = BeautifulSoup(responce.text, "html")
            self.get_city()
            EX = Extract_table(self.page)
            self.result[Country] = EX.extract()
            if city:
                self.get_all_city(Country)
        else:
            self.page = None
            self.city = None
    def get_result(self):
        """returns the result for the country"""
        return self.result[self.country]

    def get_page(self, url):
        """ get the page from the url"""
        request = requests.get(url)
        if request.status_code != 200:
            return None
        return request

    def get_city(self):
        """get all the city"""
        self.city_form = self.page.find("form", {"class": "standard_margin"})
        self.city = [values["value"] for values in self.city_form("option")]

if __name__ == "__main__":
    COUNTRY = ['Malaysia']
    results = {} 
    city = 0 #set 1 to crawl all city
    for i in COUNTRY:
        obj = API(URL, i, city)
        results[i] = obj.get_result()