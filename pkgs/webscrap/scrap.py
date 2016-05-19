#!/usr/bin/python
# -*- coding: latin-1 -*-

import requests
import bs4

root_url = 'http://avito.ma'
index_url = root_url + '/fr/maroc/'



def get_urls(product):
    prix = []
    response = requests.get(index_url+product)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    links = soup.find_all("div", {"class": "item-price"})
    for link in links:
        for price in link.contents[1].find_all("span", {"class": "price_value"}):
            prix.append(int(price.text.strip().replace(" ", "")))
    return prix

#for i in range(1,5):
#  print("------------------ Page %i ------------------")%(i)
#  index_url_p = index_url + '?o=' + str(i)
#print get_urls()