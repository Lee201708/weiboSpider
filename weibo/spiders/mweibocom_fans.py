import re
from scrapy.spider import CrawlSpider
import redis


class mweibocomFans(CrawlSpider):

    name = 'mweibocomFans'

    redis_key = 'weibo:fansURL'