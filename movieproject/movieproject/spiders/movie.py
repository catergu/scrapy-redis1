# -*- coding: utf-8 -*-
import scrapy
#先使用scrapy
#然后使用scrpay_redis

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['http://www.dy2018.com/0/']

    def parse(self, response):
        tables = response.xpath('//table[@class="tbspan"]')
        for t in tables:
            title = t.xpath('//tr[2]/a[2]/text()').extract()[0]

        pass
