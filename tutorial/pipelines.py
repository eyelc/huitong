# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import sys
import importlib
importlib.reload(sys)
import pymysql
#from scrapy.conf import settings

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class HuitongPipeline(object):
    def process_item(self, item, spider):
        return item

class huitong_jsfxPipeline(object):
    def process_item(self, item, spider):
        return item
    
#爬取名师指导数据，动态页面  
class nextSpiderPipeline(object):
    #连接数据库并写入
    def __init__(self):
        # 连接数据库
        self.client  = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  #使用自己的用户名 
            passwd='scmfa2011',  # 使用自己的密码
            db='scrapy',  # 数据库名
            charset='utf8',
            use_unicode=True)
        
#数据库游标
        self.cur = self.client.cursor()
#        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        
    def process_item(self,item,spider):
        today = time.strftime('%Y%m%d',time.localtime())
        sql = 'insert IGNORE into mszd(question,answer,questiontime,answertime,real_name,createtime,question_id,person_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        lis = (item['question'],item['answer'], item['questiontime'], item['answertime'],item['real_name'],today,item['question_id'],item['person_id'])
        
        try:
            self.cur.execute(sql,lis)
#            print("insert success")#测试语句
        except Exception as e:
#            print('Insert error:',e)
#            self.client.rollback()
            pass
        else:
            self.client.commit()
#        self.client.close()
        return item

class MeijuttPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today + 'movie.txt'
        with open(fileName,'a') as fp:
            fp.write(item['storyName'][0] + '\t' + str(item['storyState'][0]) + '\t' + str(item['tvStation'][0]) + '\t' + str(item['updateTime'][0]) + '\n')
        return item

#爬取技术垫板数据，常规页面   
class DataPipeline(object):
#写入文本文件
#    def process_item(self, item, spider):
#        today = time.strftime('%Y%m%d',time.localtime())
#        fileName = today + 'data.txt'
#        with open(fileName,'a') as fp:
#            fp.write(item['Name'][0] + '\t' + str(item['url'][0])  + '\n')
#        return item

#连接数据库并写入
#    def from_crawler(cls, crawler):
#        return cls(crawler.settings)

    def __init__(self):
        # 连接数据库
        self.client  = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  #使用自己的用户名 
            passwd='scmfa2011',  # 使用自己的密码
            db='scrapy',  # 数据库名
            charset='utf8',
            use_unicode=True)

#数据库游标
        self.cur = self.client.cursor()
#        print("-----------------------------------------------mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        
    def process_item(self,item,spider):
        today = time.strftime('%Y%m%d',time.localtime())
        sql = 'insert into huitong(title,url,author,posttime,contents,spidertime) VALUES (%s,%s,%s,%s,%s,%s)'
        lis = (item['title'],item['url'], item['author'][1].strip().lstrip().rstrip(','),item['posttime'],item['contents'],today)
        
        try:
            self.cur.execute(sql,lis)
#            print("insert success")#测试语句
        except Exception as e:
            print('------------------------------------------Insert error:',e)
#            self.client.rollback()
            pass
        else:
            self.client.commit()
#        self.client.close()
        return item
    

#爬取一牛网快讯数据，动态页面  
class yiniuPipeline(object):
    #连接数据库并写入
    def __init__(self):
        # 连接数据库
        self.client  = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  #使用自己的用户名 
            passwd='scmfa2011',  # 使用自己的密码
            db='scrapy',  # 数据库名
            charset='utf8',
            use_unicode=True)
        
#数据库游标
        self.cur = self.client.cursor()
#        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        
    def process_item(self,item,spider):
        today = time.strftime('%Y%m%d',time.localtime())
        sql = 'insert IGNORE into yiniu(yiniu_id,yiniu_title,yiniu_importance,yiniu_time,yiniu_type,createtime) VALUES (%s,%s,%s,%s,%s,%s)'
        lis = (item['yiniu_id'],item['yiniu_title'], item['yiniu_importance'],item['yiniu_time'],item['yiniu_type'], today)
        
        try:
            self.cur.execute(sql,lis)
#            print("insert success")#测试语句
        except Exception as e:
#            print('Insert error:',e)
#            self.client.rollback()
            pass
        else:
            self.client.commit()
#        self.client.close()
        return item
    
#爬取一牛网快讯分类数据，测试用
class yiniulistPipeline(object):
    #连接数据库并写入
    def __init__(self):
        # 连接数据库
        self.client  = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  #使用自己的用户名 
            passwd='scmfa2011',  # 使用自己的密码
            db='scrapy',  # 数据库名
            charset='utf8',
            use_unicode=True)
        
#数据库游标
        self.cur = self.client.cursor()
#        print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        
    def process_item(self,item,spider):
        today = time.strftime('%Y%m%d',time.localtime())
        sql = 'insert IGNORE into yiniu(yiniu_id,yiniu_title,yiniu_importance,yiniu_time,yiniu_type,createtime) VALUES (%s,%s,%s,%s,%s,%s)'
        lis = (item['yiniu_id'],item['yiniu_title'], item['yiniu_importance'],item['yiniu_time'],item['yiniu_type'], today)
        
        try:
            self.cur.execute(sql,lis)
#            print("insert success")#测试语句
        except Exception as e:
#            print('Insert error:',e)
#            self.client.rollback()
            pass
        else:
            self.client.commit()
#        self.client.close()
        return item