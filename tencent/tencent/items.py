# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    Position_Name = scrapy.Field()
    Position_Location = scrapy.Field()
    Responsibility = scrapy.Field()
    Last_Update_Time = scrapy.Field()
    Position_Src = scrapy.Field()
    Requirement = scrapy.Field()