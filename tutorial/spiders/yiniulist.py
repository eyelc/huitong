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
    name = "yiniulist"
    allowed_domains = ["www.108.cn"]
    start_urls = ['http://www.108.cn/kuaixun/more?lasttime=1544792215668&class=stock']
    
    def start_requests(self):
        url = "http://www.108.cn/kuaixun/more?lasttime=1544792215668&class=stock"
        requests = []
        formdata = {}
        request = FormRequest(url,callback=self.parse,formdata=formdata,headers=HEADERS)
        requests.append(request)
        return requests

             
    def parse(self,response):
        jsonBody = json.loads(response.body.decode('gbk').encode('utf-8'))
        jsonBody = eval(jsonBody)  #把返回的字符串转换为dict
        print(jsonBody)
        models = jsonBody['data']['data']
        Items = []
        if models:       
            for dict in models:
                Items = yiniuSpiderItem()
                if 'id' in dict.keys():             #需要判断id是否存在，因为快讯里面有数据日历，无id字段
                    Items['yiniu_id'] = dict['id']
                    Items['yiniu_title'] = self.clear_br(dict['title'])
                    Items['yiniu_importance'] = dict['importance']
                    Items['yiniu_time'] = dict['time']
                    Items['yiniu_type'] = dict['class']
                    yield Items
        else:
            print('返回空！')
            

    
            
    def clear_br(self, value):
        """
        文本中包含有<br>标签的话，传值到itme中就不会是整个文本，而是一条一条的数据
            保存到数据库的时候会报错：Operand should contain 1 column(s)
            那就要将文本里面的<br>换成其他，由于传递过来的value是一个列表list，所以用for循环把元素replace也可以
            这里用.join()方法把列表里的所有元素用逗号拼接成字符串
        """
        value = ''.join(value)
        return value