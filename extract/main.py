import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        'https://app.eload.com.br/Dashboard',
    ]

    def parse(self, response):
        title = response.css('title::text').get()
        print('Title: ', title)
