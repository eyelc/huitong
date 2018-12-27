from scrapy.http import FormRequest
from tutorial.items import nextSpiderItem
import scrapy
import json

class nextSpiderSpider(scrapy.Spider):
    name = "nextSpider"
    
    #加载自定义setting，覆盖通用setting配置
    custom_settings = {
#            'CLOSESPIDER_ITEMCOUNT': 900,  #返回多少条记录数后停止爬虫
#            'CLOSESPIDER_PAGECOUNT': 10,  #最大的抓取响应(reponses)数
            'ITEM_PIPELINES':{'tutorial.pipelines.nextSpiderPipeline':100}
            }
    
    allowed_domains = ["www.fx678.com"]
    start_urls = ['http://ask.fx678.com/ajax/answerlists.html']
    
    def start_requests(self):
        url = "http://ask.fx678.com/ajax/answerlists.html"
        requests = []
        for i in range(1,10):
            formdata = {"date":"",
                         "p":str(i),
                         "type":"1"}
            request = FormRequest(url,callback=self.parse,formdata=formdata)
            requests.append(request)
        return requests

    def parse(self, response):
        jsonBody = json.loads(response.body.decode('gbk').encode('utf-8'))
        models = jsonBody['data']
        Items = []
        for dict in models:
            Items = nextSpiderItem()
            Items['question'] = dict['question']
            Items['answer'] = self.clear_br(dict['answer'])
            Items['questiontime'] = dict['create_time']
            Items['answertime'] = dict['update_time']
            Items['real_name'] = dict['real_name']
            Items['question_id'] = dict['id']
            Items['person_id'] = dict['anal_id']
#            print(Items)
            yield Items

    def clear_br(self, value):
        """
        文本中包含有<br>标签的话，传值到itme中就不会是整个文本，而是一条一条的数据
            保存到数据库的时候会报错：Operand should contain 1 column(s)
            那就要将文本里面的<br>换成其他，由于传递过来的value是一个列表list，所以用for循环把元素replace也可以
            这里用.join()方法把列表里的所有元素用逗号拼接成字符串
        """
        value = ''.join(value)
        return value