import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json

class BookCrawlSpider(CrawlSpider):
    name = 'book_crawl'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # peraturan untuk crawling
    rules = (
        Rule(LinkExtractor(allow='catalogue/category')),
        Rule(LinkExtractor(allow='catalogue', deny='category'), callback='bookParse'),
    )
    def bookParse(self, response):
        yield {
            'judul': response.css('.product_main h1::text').get(),
            'harga': response.css('.price_color::text').get(),
        }
        pass