# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:42:36 2017

@author: mounicm
"""

import requests
from bs4 import BeautifulSoup
import json


class Extract_table:
    """ Extracts the table from the beautiful soup html page"""
    def __init__(self, page):
        self.Data = {}
        self.Table = page.find("table", {'class':'data_wide_table'}) #finding table with class name
    def extract(self):
        """A method to extract the table contents and store to a dict"""
        if not self.Table:
            return None #check if it is in the formate.
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
                self.get_all_city()
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

    def get_single_city(self, city):
        """ get table with the city name for the country"""
        country = self.country
        city_page = self.base+"/city_result.jsp?country="+country+"&city="+city
        self.city_page = BeautifulSoup(self.get_page(city_page).text, "html")
        table = Extract_table(self.city_page)
        return table.extract()

    def get_all_city(self):
        """ get the table of all the city and returns as a dict"""
        country = self.country
        self.result[country]["child"] = {}
        for city in self.city:
            print "crawling Country -> %s, city -> %s"%(country, city)
            self.result[country]["child"][city] = self.get_single_city(city)

def write_json(FILE, OBJECT):
    """ Function to store as a json file"""
    with open(FILE, 'w') as w:
        w.write(json.dumps(OBJECT))
    print "The file has written ..."

if __name__ == "__main__":
    COST = "https://www.numbeo.com/cost-of-living/"
    HEALTH = "https://www.numbeo.com/health-care/"
    BASE = HEALTH #  change to COST for cost of lining
    COUNTRY = ['Malaysia','Singapore','Australia']
    results = {}
    city = 1 #set 1 to crawl all city
    for i in COUNTRY:
        obj = API(BASE, i, city)
        results[i] = obj.get_result()
    write_json("healthcare.json",results) #uncomment to save the results.
    
