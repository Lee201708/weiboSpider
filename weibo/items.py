# -*- coding: utf-8 -*-

# Define here the models for your scraped items

from scrapy import Field,Item


class WeiboItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class InformationItem(Item):
    ID = Field()
    Name = Field()
    Sex = Field()
    FollowCount = Field()               #粉丝数
    FollowersCount = Field()            #关注数
    Description = Field()               #简介
    Verified = Field()                  #是否认证
    VerifiedReason = Field()            #认证理由
    ProfileUrl = Field()                #个人主页