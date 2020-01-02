# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SDparserItem(scrapy.Item):
    doi = scrapy.Field()
    name = scrapy.Field()
    authors = scrapy.Field()
    journal = scrapy.Field()
    year = scrapy.Field()
    volume = scrapy.Field()
    issue = scrapy.Field()
    pages = scrapy.Field()
