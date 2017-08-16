# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

USER_AGENTS = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7'


DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.CookiesMiddleware' : 100,
}


ITEM_PIPELINES = {
    # 'weibo.pipelines.WeiboPipeline' : 100,
    'weibo.pipelines.JsonWritePipeline' : 200
}


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379



