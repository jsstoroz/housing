# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Record(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field()
    owner = scrapy.Field()
    exemption_status = scrapy.Field()