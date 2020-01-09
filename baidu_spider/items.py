# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 百度图片modle类
class PictureItem(scrapy.Item):
    pic_urls = scrapy.Field()  # 每一页图片的url
