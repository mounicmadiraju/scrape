# Numbeo Web-Scraper

This folder contains a web-scraper to scrape [Numbeo](https://www.numbeo.com/cost-of-living/) for cost of living data. It will scrape all the data that Numbeo will allow you to for a given country and location (Numbeo fairly prevents scrapers, and so you won't get much if you try). It will give back all of the information that you could get for every location within a search query. 

## Usage

This scraper is built to scape Numbeo for an inputted country and location. To use it, you can simply call it from the command line as follows: 

```python 
python scrape.py   for scrapping all cost of living information
python scrape_healthcare.py     for scrapping only health care components
python scrape_pollution.py     for scrapping all pollution data
```

## API Accessible

api = API(URL, "country")

api.get_single_city("location")

## Cost Calculation by distance for Transportaion

Decision tree model in scikit-learn is implemented.
Decision tree is an appropriate model for a given problem.
Interpret a tree diagram. Tuned a decision tree model and explained how tuning impacts the model.
Advanced Machine Learning is used for *Predictions*

```python 
python transportation_prediction.py
```
