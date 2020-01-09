# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from baidu_spider.items import PictureItem

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import re


# class PictureSpiderSpider(scrapy.Spider):
class PictureSpiderSpider(CrawlSpider):
    keyword = '苹果'
    page_num = 0
    pn = page_num * 20

    name = 'picture_spider'
    allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']
    start_urls = [
        'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={}&pn={}&gsm=0&ct=&ic=0&lm=-1&width=0&height=0'.format(
            keyword, pn)]
    base_url = 'http://image.baidu.com'

    rules = (
        # .+表示前面有任意个字符  \d表示数字
        Rule(LinkExtractor(allow=r'word=.+&pn=\d&gsm=&ct=&ic=0&lm=-1&width=0&height=0'), callback="parse", follow=True),
    )

    def parse(self, response):
        # print(response.text)
        # div = response.xpath('//div[@id="imgid"]')
        # print('======div=======', div)
        # ul = div.xpath('//ul[@class="imglist"]')
        # print('===============', ul)
        # li = div.xpath('.//li[@class="imgitem"]')
        # # print('===============', li)
        # a = div.xpath('.//a[@class="imglink"]')
        # div2 = div.xpath('.//div[@class="hover"]')
        # li = response.xpath('//div[@id="imgid"]/ul/li/a/img/@src').get()
        # print('===============', li)

        html = response.text
        img_urls = re.findall('"objURL":"(.*?)",', html, re.S)
        item = PictureItem(pic_urls=img_urls)
        yield item
        next_url = response.xpath('//div[@id="page"]/a[@class="n"]/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_url + next_url,callback=self.parse)











