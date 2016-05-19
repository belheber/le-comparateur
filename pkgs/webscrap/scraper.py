#!/usr/bin/env python


from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

url_p = ['http://medicalxpress.com/news/2016-05-pfizer-blocking-drugs-lethal.html',
'http://www.scientificamerican.com/article/a-river-once-ran-through-the-sahara-graphic/',
'http://www.naturalhealth365.com/blueberries-heart-health-1827.html',
'http://www.eurekalert.org/pub_releases/2016-05/giot-lso050816.php',
'http://www.eurekalert.org/pub_releases/2016-05/uop-oof050916.php',
'http://www.eurekalert.org/pub_releases/2016-05/hzm--hfh050916.php',
'http://www.eurekalert.org/pub_releases/2016-05/tiof-nfn050916.php',
'http://www.eurekalert.org/pub_releases/2016-05/bumc-sfm050916.php',
'http://www.newsweek.com/john-oliver-last-week-tonight-scientific-studies-457343?rx=us',
'http://singularityhub.com/2016/05/11/five-exponential-trends-are-accelerating-robotics/',
'http://singularityhub.com/2016/05/12/the-personal-factory-is-here-and-it-will-bring-a-wild-new-era-of-invention/']

#url = 'http://www.newsweek.com/john-oliver-last-week-tonight-scientific-studies-457343?rx=us'

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
f = open('../templates/compareprice/page.html','w')
f.write(""" {% extends 'compareprice/index.html' %} """)
f.write("\n"+""" {% block content %} """)

def scrape(link, attribute):
  driver.get(link)
  sleep(3)
  s = BeautifulSoup(driver.page_source)
  data = s.find(attribute)
  formt_data = data.string.encode("cp437", "ignore")
  f.write("<a href=")
  f.write(""" "%s"> """ %(link))
  f.write(formt_data+"</a>")
  f.write("</br>")
  return formt_data


def link_scrap():
  for url in url_p:
    scrape(url, "title")
  driver.quit()
  f.write("\n"+""" {% endblock content %} """)
  f.close()
