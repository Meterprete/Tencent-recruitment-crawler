# -*- coding: utf-8 -*-
import scrapy
import json
from tencent.items import TencentItem

page = 1


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?countryId=1&parentCategoryId=40001&pageIndex=1&pageSize=10']

    def parse(self, response):
        text = response.text
        data_list = json.loads(text)['Data']['Posts']
        for data_dict in data_list:
            item = TencentItem()
            item['Position_Name'] = data_dict['RecruitPostName']
            item['Position_Location'] = data_dict['CountryName'] + data_dict['LocationName']
            item['Responsibility'] = data_dict['Responsibility']
            item['Last_Update_Time'] = data_dict['LastUpdateTime']
            item['Position_Src'] = data_dict['PostURL']

            '''另外请求详细招聘信息'''
            url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId=" + data_dict['PostId']
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item},
                dont_filter=False
            )

        '''翻页请求'''
        global page
        print("已抓取完第{}页".format(page))
        page = page + 1
        if (page * 10 - 9) <= int(json.loads(text)['Data']['Count']):
            next_url = "https://careers.tencent.com/tencentcareer/api/post/Query?countryId=1&parentCategoryId=40001&pageIndex={}&pageSize=10".format(
                page)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=False
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item['Requirement'] = json.loads(response.text)['Data']['Requirement']
        yield item
