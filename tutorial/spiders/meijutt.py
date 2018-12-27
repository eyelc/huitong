# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import MeijuttItem

class MeijuttSpider(scrapy.Spider):
    name = 'meijutt'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        items = []
        for sel in response.xpath('//ul[@class="top-list  fn-clear"]/li'):
            item = MeijuttItem()
            item['storyName'] = sel.xpath('./h5/a/text()').extract()
            item['storyState'] = sel.xpath('./span[1]/font/text()').extract()
            if item['storyState']:
                pass
            else:
                item['storyState'] = sel.xpath('./span[1]/text()').extract()
            item['tvStation'] = sel.xpath('./span[2]/text()').extract()
            if item['tvStation']:
                pass
            else:
                item['tvStation'] = [u'未知']
            item['updateTime'] = sel.xpath('./div[2]/text()').extract()
            if item['updateTime']:
                pass
            else:
                item['updateTime'] = sel.xpath('./div[2]/font/text()').extract()
            items.append(item)
            

        return items
    