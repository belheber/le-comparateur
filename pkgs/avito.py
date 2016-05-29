#!/usr/bin/python

import requests
import bs4

root_url = 'http://avito.ma'
index_url = root_url + '/fr/maroc/'
product = 'samsung'
url = index_url + product

products_link = []
products_price = []
products_title = []


def get_urls(url):
  print url
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text, "lxml")
  product_items = soup.find_all("div",{"class":"item li-hover"})
  for pro in product_items:
    products_link.append(pro.a['href'].encode('utf-8'))
    products_title.append(pro.h2.text.strip().encode('utf-8'))

    price = pro.find("div", {"class": "item-price"}).find('span',{"class":"price_value"})
    if None == price or '' == price.text.strip():
      price = 0
    else :
       price = price.text.replace(" ","").encode('utf-8')
    products_price.append(int(price))
  


def browse_product(url,among_price):
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text, "lxml")
  if among_price != 0:
    among_price = soup.h2.span['title']
  panel = soup.find('div',{'class':'span20'})
  body = soup.find('div',{'class':'span10'}).text
  body = " ".join(body.split()).encode('utf-8')
  nbr_view = panel.contents[1].span.text.split()[1]
  location = panel.contents[3].h2.text.strip().encode('utf-8')
  date = panel.contents[3].ul.abbr['title']
  author = panel.contents[3].strong.text.encode('utf-8')
  
  print author
  print location
  print date
  print nbr_view
  print among_price
  print body[:150]+' ... view more'

for i in range(47, 50):
  print("------------------ Page %i ------------------"%(i))
  index_url_p = url + '?o=' + str(i)
  get_urls(index_url_p)
  
j = 1
for i, link in enumerate(products_link):
  price = products_price[i]

  if price > 1500:
    print '-------------PRODUCT %i------------------'%(j)
    print products_title[i]
    print link
    print price
    j = j +1
    browse_product(link, products_price[i])  
