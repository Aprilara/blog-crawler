#-*-coding:utf-8-*-

'''@author:younghz
   @description:代理IP中间件。
                使用settings.py的PROXIES中设置的代理IP（代理时间长会失效，需要手动查找更新）
'''

import random
from scrapy import log

#也可以通过下面两个（1）标注的部分实现效果但是不符合插件的编写规则。
#（1）from scrapy.conf import settings

class ProxyMiddleware(object):

    def __init__(self, proxy):
        self.proxy = proxy

    @classmethod
    def from_settings(cls, settings):
        proxy_list = settings.get('PROXIES')
        return cls(proxy_list)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_request(self, request, spider):
        pro = random.choice(self.proxy)

        #（1）pro = random.choice(settings.get('PROXIES'))
        if pro:
            #print '++++++++++++++++++++++++++++++++'
            #print pro
            log.msg(pro, level=log.INFO)
            request.meta['proxy'] = pro