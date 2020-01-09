# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from baidu_spider import settings
import os

headers = {

"Host":"mm.chinasareview.com",
"Proxy-Connection":"keep-alive",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"__jsluid=6dad86b537349828028bbed3237da97a",
"If-None-Match": "f67cd360b83ed31:104f",
"If-Modified-Since": "Fri, 06 Oct 2017 15:32:54 GMT",
}

class BaiduSpiderPipeline(object):

    def process_item(self, item, spider):

        if 'pic_urls' in item:  # 如何‘图片地址’在项目中
            images = []  # 定义图片空集

            #./meizi
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)
            #不存在就创建./meizi
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print("文件夹创建成功")


            for image_url in item['pic_urls']:
                # http://pic33.photophoto.cn/20141120/0020033666035745_b.jpg
                # print("image_url===",image_url)

                # us = image_url.split('/')[3:]
                # image_file_name = '_'.join(us)
                image_file_name = image_url.split('/')[-1]
                file_path = '%s/%s' % (dir_path, image_file_name)

                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                response = requests.get(image_url,headers=headers)
                # 如果请求成功
                if response.status_code == 200:

                    with open(file_path, 'wb') as f:

                        f.write(response.content)
                else:
                    print("图下失败url==",image_url)
        return item
