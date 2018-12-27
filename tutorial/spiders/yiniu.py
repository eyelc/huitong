from scrapy.http import FormRequest
from tutorial.items import yiniuSpiderItem
import scrapy
import json

HEADERS = {
    'Host': 'www.108.cn',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'http://www.108.cn/kuaixun/index/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
    
class yiniuSpider(scrapy.Spider):
    name = "yiniu"
    
    #加载自定义setting，覆盖通用setting配置
    custom_settings = {
#            'CLOSESPIDER_ITEMCOUNT': 900,  #返回多少条记录数后停止爬虫
            'CLOSESPIDER_PAGECOUNT': 10,  #最大的抓取响应(reponses)数
            'ITEM_PIPELINES':{'tutorial.pipelines.yiniuPipeline':100}
            }
    
    allowed_domains = ["www.108.cn"]
    start_urls = ['http://www.108.cn/kuaixun/index']
    
    def start_requests(self):
        url = "http://www.108.cn/kuaixun/index"
        requests = []
        formdata = {}
        request = FormRequest(url,callback=self.parse,formdata=formdata,headers=HEADERS)
        requests.append(request)
        return requests

    def parse(self, response):
        jsonBody = json.loads(response.body)
        mydict = jsonBody['data']
#        print(mydict.keys())
        lastkxid = []         
        for key in mydict:                          #循环取快讯所有类别,global,oil,forex,gold,stock
            models = mydict[key]['data']
            lastkxid.append(mydict[key]['lastkxid'])   #快讯分类lastkxid，从首页时用于构建下一个url,
#            print(mydict[key]['lastkxid'])
            Items = []
            for dict in models:
                Items = yiniuSpiderItem()
                if 'id' in dict.keys():             #需要判断id是否存在，因为快讯里面有数据日历，无id字段
                    Items['yiniu_id'] = dict['id']
                    Items['yiniu_title'] = self.clear_br(dict['title'])
                    Items['yiniu_importance'] = dict['importance']
                    Items['yiniu_time'] = dict['time']
                    Items['yiniu_type'] = dict['class']
                    yield Items
#            print(lastkxid)
            #根据分类lastkxid构建新的url         
            new_url = ''.join(['http://www.108.cn/kuaixun/more?lasttime=',str(mydict[key]['lastkxid']),'&class=',str(key)])

            # callback 回调函数，页面进行解析
            request = scrapy.Request(url=new_url, callback=self.parse2,headers=HEADERS)
            yield request
                    
#分类快讯返回json不同于首页结构，需要重新处理                
    def parse2(self,response):
        jsonBody = json.loads(response.body.decode('gbk').encode('utf-8'))
        jsonBody = eval(jsonBody)  #把返回的字符串转换为dict
        lastlistid = jsonBody['data']['lastid']  #返回的id，以此构建新的url
#        print(jsonBody)
        models = jsonBody['data']['data']
        Items = []
        if models:#返回数据不为空执行
            for dict in models:
                Items = yiniuSpiderItem()
                if 'id' in dict.keys():             #需要判断id是否存在，因为快讯里面有数据日历，无id字段
                    Items['yiniu_id'] = dict['id']
                    Items['yiniu_title'] = self.clear_br(dict['title'])
                    Items['yiniu_importance'] = dict['importance']
                    Items['yiniu_time'] = dict['time']
                    Items['yiniu_type'] = dict['class']
                    yield Items
            new_url = ''.join(['http://www.108.cn/kuaixun/more?lasttime=',str(lastlistid),'&class=',str(dict['class'])])
    
            yield scrapy.Request(url=new_url, callback=self.parse2,headers=HEADERS) 
        else:
            print('返回为空，取完数据!')

           
    def clear_br(self, value):
        """
        文本中包含有<br>标签的话，传值到itme中就不会是整个文本，而是一条一条的数据
            保存到数据库的时候会报错：Operand should contain 1 column(s)
            那就要将文本里面的<br>换成其他，由于传递过来的value是一个列表list，所以用for循环把元素replace也可以
            这里用.join()方法把列表里的所有元素用逗号拼接成字符串
        """
        value = ''.join(value)
        return value