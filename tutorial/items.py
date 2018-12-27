# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class MeijuttItem(scrapy.Item):
    # define the fields for your item here like:
    storyName = scrapy.Field()
    storyState = scrapy.Field()
    tvStation = scrapy.Field()
    updateTime = scrapy.Field()
    
class DatatItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    posttime = scrapy.Field()
    contents = scrapy.Field()
    
class HuitongItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    questiontime = scrapy.Field()
    answer = scrapy.Field()
    answertime = scrapy.Field()
    teacher = scrapy.Field()
    posttime = scrapy.Field()

class nextSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    answer = scrapy.Field()  
    questiontime = scrapy.Field()  
    answertime = scrapy.Field()  
    real_name = scrapy.Field()  
    question_id = scrapy.Field()  
    person_id = scrapy.Field()  
    
class QA_spiderItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    answer = scrapy.Field()  
#    questiontime = scrapy.Field()  
#    answertime = scrapy.Field()  
#    real_name = scrapy.Field()  
#    question_id = scrapy.Field()  
#    person_id = scrapy.Field()  
    
class yiniuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    yiniu_id = scrapy.Field()
    yiniu_title = scrapy.Field()  
    yiniu_importance = scrapy.Field()  
    yiniu_time = scrapy.Field()  
    real_name = scrapy.Field()  
    yiniu_type = scrapy.Field()  

    