import sys
from os import path
import os
import requests #Web client to scrape data
from requests.utils import quote
from bs4 import BeautifulSoup as soup #helps parsing HTML in Python
sys.path.append(path.dirname(path.dirname(path.abspath('base.py'))))
from base import Store

class Walmart:
    def __init__(self):
        self.url="https://www.walmart.com/"

    def search(self,item):
        item = quote(item)
        my_url = self.url + "search/?query="+item
        urlClient = requests.get(my_url)  # Opens connection, grabs the webpage and downloads it
        page_html = urlClient.content
        urlClient.close()
        #Parsing html
        page_soup=soup(page_html,"html.parser")
        #grabs each product
        containers = page_soup.find_all("div",{"class":"search-result-gridview-item-wrapper"})
        # print(len(containers))
        storeObj = Store()
        for container in containers:
            out_of_stock = len(containers[0].find_all("div",{"class":"product-sub-title-block product-out-of-stock"}))!=0
            if not out_of_stock:
                store = Store()
                store.store_name = 'Walmart'
                store.title = container.img["alt"]
                store.image_url = container.img["data-image-src"]
                store.product_url =self.url+container.a["href"]
                store.price =container.find_all("span", {"class": "visuallyhidden"})[-1].text
                storeObj.add_item(store)
        return storeObj.generate_json()