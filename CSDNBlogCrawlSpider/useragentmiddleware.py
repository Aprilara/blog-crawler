# -*-coding:utf-8-*-

"""避免被ban策略之一：使用useragent池。

使用注意：需在settings.py中进行相应的设置。
"""

import random
from scrapy import log
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    @classmethod
    def from_settings(cls, settings):
        ua_list = settings.get('user_agent_list')
        return cls(ua_list)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent)
        if ua:
            log.msg('Current UserAgent: '+ua, level=log.INFO)    #记录
            request.headers.setdefault('User-Agent', ua)




