import scrapy

class CnblogItem(scrapy.Item):
    title = scrapy.Field()  #定义爬取的标题
    link = scrapy.Field()   #定义爬取的标题