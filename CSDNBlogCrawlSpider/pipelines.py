# -*- coding:utf-8 -*-

import json
import codecs

class CsdnblogcrawlspiderPipeline(object):

    def __init__(self):
        self.file = codecs.open('csdnblog_data.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        """item处理函数。

        Args：
            item:items中定义数据结构。
            spider:爬虫。

        Returns:
            item

        Raises:
        """
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode('unicode_escape'))

        return item
