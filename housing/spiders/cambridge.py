# -*- coding: utf-8 -*-
import scrapy
from housing.items import Record
from bs4 import BeautifulSoup

class CambridgeSpider(scrapy.Spider):
    name = 'cambridge'
    allowed_domains = ['cambridgema.gov/propertydatabase/']
    start_urls = ['https://www.cambridgema.gov/propertydatabase/'+str(i) for i in range(22,25000)]

    def parse(self, response):
        if response.status == 404:
            return
        else:
            self.logger.info('%s responded!', response.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = [a.text for a in soup.find_all('th')]
            content = [c.text for c in soup.find_all('td')]
            yield dict(zip(titles, content))