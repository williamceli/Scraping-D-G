# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:23:01 2018

@author: WilliamCeli
"""

import requests
from bs4 import BeautifulSoup


base_url = "https://store.dolcegabbana.com/en/women/clothing/dresses/?page="
prices = []

for i in range(1,100):
    url = base_url + str(i)
    with requests.session() as s:
        s.headers['user-agent'] = 'Mozilla/5.0'
        try:     
                r = s.get(url,timeout = 25)
        except Exception as e:
            print(e)
        st = r.status_code
        print('STATUS: ' + str(st))
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            divs = soup.findAll('div', attrs = {"class":"b-product_price"})
            for d in divs:
                prices.append(d.text)
        elif r.status_code == 404:
            print("Sorry, No more pages to show") 
            break
                
