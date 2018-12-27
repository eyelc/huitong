# -*- coding: utf-8 -*-
#from scrapy.cmdline import execute
#import sys
import os

import time

while True:
    os.system("scrapy crawl nextSpider")
    time.sleep(600)  #每隔一天运行一次 24*60*60=86400s
    
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(["scrapy", "crawl", "data"])
## -*- coding: utf-8 -*-

