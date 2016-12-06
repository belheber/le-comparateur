#!/usr/bin/python

import requests
import bs4



def get_urls(product):
  root_url = 'http://avito.ma'
  index_url = root_url + '/fr/maroc/'
  url = index_url + product
  product = {}
  product_list = []
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text, "lxml")
  pr_items = soup.find_all("div",{"class":"item li-hover "})
  for pro in pr_items:
    price = pro.find("div", {"class": "item-price"}).find('span',{"class":"price_value"})      
    if None == price or '' == price.text.strip():
      price = 0
    else :
      price = price.text.replace(" ","").encode('utf-8') 
    product['link'] = pro.a['href'].encode('utf-8')
    product['name'] = pro.h2.text.strip().encode('utf-8')
    product['price'] = int(price)
    product_list.append(product.copy())
  return product_list

def get_products(url_pro, among_price):
  prod_data = {}
  prod_data['img_prod'] = []
  response = requests.get(url_pro)
  soup = bs4.BeautifulSoup(response.text, "lxml")
  if among_price != 0:
    among_price = soup.h2.span['title']
  panel = soup.find('div',{'class':'span20'})
  body = soup.find('div',{'class':'span10'}).text
  prod_data['body'] = " ".join(body.split()).encode('utf-8')
  prod_data['nbr_view'] = panel.contents[1].span.text.split()[1]
  prod_data['location'] = panel.contents[3].h2.text.strip().encode('utf-8')
  prod_data['date'] = panel.contents[3].ul.abbr['title']
  prod_data['author'] = panel.contents[3].strong.text.encode('utf-8')
  prod_data['price'] = among_price
  imgs = soup.find('div', {'class':'carousel-inner'})
  if imgs != None:
    imgs = imgs.find_all('img')
    for im in imgs:
      if im.has_attr('src'):
        link_image = im['src']
      else:
        link_image = im['data-lazyload']
      prod_data['img_prod'].append(link_image) 
  else:
    link_image = '#'
    prod_data['img_prod'].append(link_image) 
  return prod_data

# pr =  get_urls('iphone')
# for p in pr:
#   print p['name']
#   pro_data = get_products(p['link'], p['price'])
#   link = pro_data['img_prod']
#   print 'nombre produits : ', len(link)
#   print link


