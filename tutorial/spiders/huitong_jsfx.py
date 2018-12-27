# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import DatatItem


class HuigongJsfxSpider(CrawlSpider):
    name = 'huitong_jsfx'
    allowed_domains = ['fx678.com']
    start_urls = ['http://news.fx678.com/column/jsfx/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="pagination-m"]')),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="item clearfix"]/a[@class="content"]/@href'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
#        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item = DatatItem()
        item = {}
        item['title'] = response.xpath('//div[@class="article-cont"]/h1/text()').extract()
        item['url'] = response.url
        item['posttime'] = response.xpath('//div[@class="article-cont"]/div[@class="details"]/i/text()').extract()
        item['author'] = response.xpath('//div[@class="article-cont"]/div[@class="details"]/a/text()').extract()
        item['content'] = response.xpath('//div[@class="content"]/text()').extract()
        return item
