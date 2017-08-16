# -*- coding: utf-8 -*-

# Define your item pipelines here
import json

class WeiboPipeline(object):
    def process_item(self, item, spider):
        return item

'''将item保存到json文件中，如果用json.load()读取json数据的话，需要手动删除结尾的   ,\n    然后前后加上 [ ]
   或者将文件读出来，再通过 rstrip(',\n'),在首位加上  '['  和  ']' ,再写入 json 文件
'''
class JsonWritePipeline(object):
    def open_spider(self,spider):
        self.file = open('json/' + spider.name +'.json','a+',encoding='utf-8')

    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False) + ','+'\n'
        self.file.write(line)
        return item

    def close_spider(self,spider):
        self.file.close()


