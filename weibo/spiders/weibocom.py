from scrapy.spider import CrawlSpider

class weibocom(CrawlSpider):

    name = 'weibocom'

    start_urls = {
        # 'http://weibo.com/p/1035053217179555/follow?relate=fans&from=103505&wvr=6&mod=headfans&current=fans#place'
        'http://m.weibo.cn/u/1934363217?uid=1934363217&luicode=10000011&lfid=1005051934363217'
    }

    def parse(self,response):
        html = response.body
        html = html.decode('utf-8')
        print(html)




    '''笔记：
        weibo.com中，粉丝的相关数据是直接放在响应的html中

    '''