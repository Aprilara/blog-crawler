# -*- coding:utf-8 -*-

from scrapy.item import Item, Field

class CsdnblogcrawlspiderItem(Item):
    """保存提取信息数据结构。

    Attributes:
    """

    blog_name = Field()
    blog_url = Field()

