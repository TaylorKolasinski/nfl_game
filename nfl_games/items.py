# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NflGamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    first_q = scrapy.Field()
    second_q = scrapy.Field()
    third_q = scrapy.Field()
    fourth_q = scrapy.Field()	
    home_score = scrapy.Field()
    visiting_score = scrapy.Field()
    home_team = scrapy.Field()
    visiting_team = scrapy.Field()
    final = scrapy.Field()

    pass
