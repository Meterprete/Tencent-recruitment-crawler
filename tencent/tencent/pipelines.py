# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re


class TencentPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        self.connect = client['tencent']['hr']

    def process_item(self, item, spider):
        item['Responsibility'] = self.process_content(item['Responsibility'])
        item['Requirement'] = self.process_content(item['Requirement'])
        self.connect.insert(dict(item))
        return item

    def process_content(self, content):
        content = re.sub(r"\r\n|\s", "", content)
        # print(content)
        return content
