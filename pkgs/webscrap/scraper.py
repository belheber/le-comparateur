#!/usr/bin/env python

import re
import urlparse

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

link = 'http://medicalxpress.com/news/2016-05-pfizer-blocking-drugs-lethal.html'

class TaleoJobScraper(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def scrape_job_links(self):
        self.driver.get(link)
        sleep(3)

        s = BeautifulSoup(self.driver.page_source)
        title = s.title.string

            #r = re.compile(r'jobdetail\.ftl\?job=\d+$')
        #print s
        f = open('page.html','w')
        f.write(str(s))
        f.close()

        
        return title


    def scrape(self):
        return self.scrape_job_links()

        self.driver.quit()

