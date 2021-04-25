import scrapy


class MylocationSpider(scrapy.Spider):
    name = 'mylocation'
    allowed_domains = ['mylocation.org']
    start_urls = ['http://mylocation.org/']

    def parse(self, response):
        print("response:", response.text)
        # yield ''
