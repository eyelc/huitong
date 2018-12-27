# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tutorial.items import DatatItem


 
class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['fx678.com']
    start_urls = ['http://news.fx678.com/column/jsfx/1']  #只有一条开始地址
#
#添加多条有规律地址
#    start_urls = []
#    for i in range(1,3):
#        url = 'http://news.fx678.com/column/jsfx/'
#        url = url + str(i)
#        start_urls.append(url)
#    start_urls
    

    def parse(self, response):
#        print('-------------------------------------Start----------------------------------------')
#        print(response.url)
#        print('\n')
         
# 爬取每条地址对应页面数据
#        for sel in response.xpath('//li[@class="item clearfix"]'):
#            item = DatatItem()
#            item['title'] = sel.xpath('./a[@class="content"]/h3/text()').extract()
#            item['url'] = sel.xpath('./a[@class="content"]/@href').extract()
#            item['posttime'] = sel.xpath('./div[@class="details clearfix"]/i/text()').extract()
#            item['author'] = sel.xpath('./div[@class="details clearfix"]/a/span/text()').extract()
#            
#         
#            yield item
        
        
       #拼接多条规律地址 
        i = 2 
        while i<=10:
            next_url="http://news.fx678.com/column/jsfx/" + str(i)
            i = i +1
            yield Request(url=next_url,callback=self.parse)
            
        item_url = response.xpath('//li[@class="item clearfix"]/a[@class="content"]/@href').extract()
        for url in item_url:
#            print('-----------------------------------------------------------')
#            print(url)
#            print('-----------------------------------------------------------')
            yield Request(url,callback=self.parse_item)
            
    def parse_item(self,response):
#        item_url = response.xpath('//div[@class="article-cont"]').extract()          
#        for sel in item_url:
        item = DatatItem()
        item['title'] = response.xpath('//div[@class="article-cont"]/h1/text()').extract()
        item['url'] = response.url
        item['posttime'] = response.xpath('//div[@class="article-cont"]/div[@class="details"]/i/text()').extract()
        item['author'] = response.xpath('//div[@class="article-cont"]/div[@class="details"]/a/text()').extract()
        item['contents'] = self.clear_br(response.xpath('//div[@class="content"]/text()').extract())
               
        yield item
        
    def clear_br(self, value):
        """
        文本中包含有<br>标签的话，传值到itme中就不会是整个文本，而是一条一条的数据
            保存到数据库的时候会报错：Operand should contain 1 column(s)
            那就要将文本里面的<br>换成其他，由于传递过来的value是一个列表list，所以用for循环把元素replace也可以
            这里用.join()方法把列表里的所有元素用逗号拼接成字符串
        """
        value = ','.join(value)
        return value
