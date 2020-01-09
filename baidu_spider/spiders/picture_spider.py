# -*- coding: utf-8 -*-
import scrapy


class PictureSpiderSpider(scrapy.Spider):
    name = 'picture_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
