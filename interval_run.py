#usr/bin/python

import os
import time

times = 0
while True:
    times += 1
    print "start crawl.It is the %d times." %times
    os.popen('scrapy crawl CSDNBlogCrawlSpider --set LOG_FILE=log')
    print "end crawl."
    time.sleep(10)

