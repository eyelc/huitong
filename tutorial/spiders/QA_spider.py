from scrapy.http import FormRequest
from tutorial.items import QA_spiderItem
import scrapy
import json

class nextSpiderSpider(scrapy.Spider):
    name = "QA_spider"
    allowed_domains = ["eastmoney.com"]
    start_urls = ['http://ask.eastmoney.com/wenda/QAInterfaceRead.aspx']
    
    def start_requests(self):
        url = "http://ask.eastmoney.com/wenda/QAInterfaceRead.aspx"
        requests = []
        for i in range(1,10):
#            unicornHeader = {
#            'Host': 'ask.eastmoney.com',
#            'Origin': 'http://ask.eastmoney.com',
#            'Referer': 'http://ask.eastmoney.com/detail.html?qid=197899100333674496',
#            }
#
#            formdata = {'url':'QAApi/QA/GetQuestionDetail',
#                        'key':'{"QId":"197899100333674496","PageNo":'+ str(i) +',"PageSize":40,"OnlyBest":0,"AppId":"EM_PC_Web"}'                      
#                        }
            unicornHeader = {
            'Host': 'ask.eastmoney.com',
            'Origin': 'http://ask.eastmoney.com',
            'Referer': 'http://ask.eastmoney.com',
            }

            formdata = {'url':'QAApi/QA/GetQAList',
                        'key':'{"PageNo":'+ str(i) +',"PageSize":20,"SortType":0,"AppId":"EM_PC_Web"}'                      
                        }
            request = FormRequest(
                    url,
                    headers = unicornHeader,
                    callback=self.parse,
                    method = 'POST',
                    formdata=formdata)
            requests.append(request)
        return requests

    def parse(self, response):
        jsonBody = json.loads(response.body)
        QAnswer = jsonBody['Data']['QAList']
        
        for dz in QAnswer:
            myquestion = dz.get('Question').get('Summary')
            myqid = dz.get('Question').get('QId')
            print( myqid + '_' + myquestion)
            

#        myquestion = QAnswer.get('QuestionUser').get('Question').get('Content')
#        print('-----------------------------------------------------------------')
#        print(myquestion)
#        print('-----------------------------------------------------------------')
#        answer_data = QAnswer.get('AnswerUserList')
#        for dz in answer_data:
#            myanswer = dz.get('Answer').get('Content')
#            print(myanswer)



