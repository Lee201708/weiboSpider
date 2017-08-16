from scrapy.spider import CrawlSpider
from scrapy import FormRequest
from scrapy import Request
import redis
import re
import math

from weibo.items import InformationItem


class weibo(CrawlSpider):

    name = 'mweibocom'
    start_urls = [1337970873,
                 # 2995631244, 5878659096,
                 # 5235640836, 5676304901, 5871897095, 2139359753, 5579672076, 2517436943, 5778999829, 5780802073, 2159807003,
                 # 1756807885, 3378940452, 5762793904, 1885080105, 5778836010, 5722737202, 3105589817, 5882481217, 5831264835,
                 # 2717354573, 3637185102, 1934363217, 5336500817, 1431308884, 5818747476, 5073111647, 5398825573, 2501511785,
                 ]
    redis_keys = 'weibo:userID'
    # r = redis.Redis()

    def start_requests(self):
        for num in self.start_urls:
            url_message = 'http://m.weibo.cn/container/getIndex?uid={0}&luicode=20000174&type=uid&value={0}&containerid=100505{0}'.format(num)   #用户信息
            # url_content = 'http://m.weibo.cn/container/getIndex?uid={0}&luicode=20000174&type=uid&value={0}&containerid=107603{0}'.format(num)   #用户发过的微博

            # return [FormRequest(url_message,callback=self.parse)]
            # url = 'http://weibo.cn/hutuheshang?page=3'                    #weubo.cn不能用这个cookie
            yield Request(url_message,self.InfoParse)                       #去抓取用户个人信息
            # yield Request(url_content,self.MessageParse)                    #去抓用户的微博

    def InfoParse(self, response):
        html = response.body
        html = html.decode('unicode-escape')
        Info = InformationItem()
        ID = re.findall('"id":(.*?),',html,re.S)                            #用户唯一ID
        Name = re.findall('"screen_name":"(.*?)",',html,re.S)                 #名字
        Sex = re.findall('"gender":"(.)",', html, re.S)                     #性别
        FollowCount = re.findall('"follow_count":(.*?),',html,re.S)         #粉丝数
        FollowersCount = re.findall('"followers_count":(.*?),',html,re.S)   #关注数
        Description = re.findall('"description":"(.*?)",',html,re.S)
        ProfileUrl = re.findall('"profile_url":"(.*?)",',html,re.S)              #个人主页
        Verified =re.findall('"verified":(.*?),',html,re.S)                 #是否认证
        VerifiedReason = re.findall('"verified_reason":"(.*?)",',html,re.S) #认证简介
        #获取粉丝页和关注人 链接
        # fans_scheme = re.findall('"fans_scheme":"(.*?)",',html,re.S)[0]        #粉丝链接
        # fans_scheme_handle = fans_scheme.replace('\/','/')
        # fans_scheme_handle = fans_scheme_handle.replace('p/index','container/getIndex')
        # fans_scheme_handle = fans_scheme_handle.replace('fansrecomm','fans')
        # follow_scheme = re.findall('"follow_scheme":"(.*?)",',html,re.S)[0]    #关注人链接
        # follow_scheme_handle = follow_scheme.replace('\/','/')
        # follow_scheme_handle = follow_scheme_handle.replace('p/index','container/getIndex')
        # follow_scheme_handle = follow_scheme_handle.replace('followersrecomm','followers')

        # self.r.lpush('weibo:fansURL',fans_scheme_handle)


        Info['ID'] = ID[0]
        Info['Name'] = Name[0]
        Info['Sex'] = Sex[0]
        Info['FollowCount'] = FollowCount[0]
        Info['FollowersCount'] = FollowersCount[0]
        Info['Description'] = Description[0]
        Info['Verified'] = Verified[0]
        Info['ProfileUrl'] = ProfileUrl[0].replace('\/','/')
        if VerifiedReason:  Info['VerifiedReason'] = VerifiedReason[0]
        yield Info
        #计算粉丝的页数，每页20个
        # FansPageCount = math.ceil(int(FollowCount[0]) / 20)
        # for page in range(1,FansPageCount+1):
        #     yield Request(url = fans_scheme_handle + '&page=%d'%page,callback=self.FansParse)         #去抓粉丝
        # FollowersPageConut = math.ceil(int(FollowersCount[0]) / 20)
        # for page in range(1,FollowersPageConut+1):
        #     yield Request(url = follow_scheme_handle + '&page=%d'%page,callback=self.FollowParse)     #去抓关注人

    def MessageParse(self,response):
        pass


    def FansParse(self,response):
        pass

    def FollowParse(self,response):
        pass






