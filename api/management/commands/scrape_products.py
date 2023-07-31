from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = 'Run the Scrapy spider and store scraped data in PostgreSQL database.'

    def handle(self, *args, **options):
        # Replace 'YourSpiderName' with the actual name of your Scrapy spider
        spider_name = 'books'

        # Run the Scrapy spider
        process = CrawlerProcess(get_project_settings())
        process.crawl(spider_name)
        process.start()