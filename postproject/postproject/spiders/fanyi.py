# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_redis.spiders import Spider,CrawlSpider

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']
    #post请求的接口
    start_urls = ['http://fanyi.baidu.com/sug/']

    def parse(self, response):

        text = response.text
        data = json.loads(text,encoding = 'utf-8')
        print(data)

        yield data

        pass


    #自动调用
    #scrapy.Request()------>get请求
    #scrapy.FormRequest()------>post请求

    #如果想要实现post请求，重写发起请求方法

    def start_requests(self):
        url = self.start_urls[0]
        form = {'kw':'world'}
        request = scrapy.FormRequest(url = url,formdata = form,callback = self.parse)

        yield request

        return super().start_requests()