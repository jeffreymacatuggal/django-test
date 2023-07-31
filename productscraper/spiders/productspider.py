import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from productscraper.items import ProductItem
from productscraper.itemloaders import ProductLoader

class BooksSpider(scrapy.Spider):
    name = 'books'

    def start_requests(self):
        URL = 'https://books.toscrape.com/'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):

        products = response.css('article.product_pod')

        for product in products:

            product = ProductLoader(item=ProductItem(), selector=product)
            product.add_css('name', 'h3 > a::attr(title)')
            product.add_css('price', '.price_color::text')
            product.add_css('url', 'div.image_container a::attr(href)')
            product.add_css('image_url', 'div.image_container a img::attr(src)')

            yield product.load_item()

        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)