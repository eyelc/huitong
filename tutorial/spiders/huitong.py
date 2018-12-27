# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import HuitongItem
from urllib import parse

class HuitongSpider(scrapy.Spider):
    name = 'huitong'
    allowed_domains = ['fx678.com']
    
##取名师指导
#    start_urls = ['http://ask.fx678.com/qalist/1.html']
#
#    def parse(self, response):
#        #取汇通名师指导 
#        for sel in response.xpath('//div[@class="QA_det"]'):
#            item = HuitongItem()
#            item['question'] = sel.xpath('./div[1]/a/text()').extract()
#            item['answer'] = sel.xpath('./div[2]/a/text()').extract()
##            print(item) 
#            yield item
#        pass

#技术分析
    start_urls = ['http://news.fx678.com/column/jsfx']

    def parse(self, response):
        #取汇通名师指导 
        for url in response.xpath('//li[@class="item clearfix"]/a[@class="content"]/@href').extract():
            yield scrapy.Request(url, callback=self.get_info)
            

#            item = HuitongItem()
#            item['question'] = sel.xpath('./a[@class="content"]/h3/text()').extract()
#            item['answer'] = sel.xpath('./a[@class="content"]/@href').extract()
#            print(item) 
#            yield item
#        pass
    
#        nexturl =  response.xpath('//*[contains(@class,"pagination-m")]/@href').extract()
        nexturl =  response.css('pagination-m::href').extract()
        if nexturl: # 判断是否存在下一页
#            nexturl ='http://news.fx678.com' + nexturl[0]
            nexturl = parse.urljoin(response.url,nexturl[1])
            print('------------------------------------------')
            print(response.url)
            print(nexturl)
            print('------------------------------------------')
            yield scrapy.Request(url=nexturl, callback=self.parse)
            
    def get_info(self,response):
        title = response.xpath('//div[@class="article-cont"]/h1/text()').extract()
        print(title)