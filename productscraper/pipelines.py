# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class PriceToFloatPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## check is price present
        if adapter.get('price'):
            # Convert the 'price' to a float
            float_price = float(adapter['price'])
            adapter['price'] = float_price
            return item
        else:
            # drop item if no price
            raise DropItem(f"Missing price in {item}")


class DuplicatesPipeline:

    def __init__(self):
        self.names_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['name'] in self.names_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.names_seen.add(adapter['name'])
            return item


class SavingToPostgresPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host="containers-us-west-55.railway.app",
            database="railway",
            user="postgres",
            password="oSMyfY8DgHhWhnP32vBJ",
            port="6771"
            )

        self.cure = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_in_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_in_db(self, item):

        name = item['name']
        price = item['price']
        url = item['url']
        image_url = item['image_url']

        insert_query = "INSERT INTO api_product_data (name, price, url, image_url) VALUES (%s, %s, %s, %s);"
        data = (name, price, url, image_url)
        try:

            # Start the transaction
            self.cure.execute("BEGIN;")

            self.cure.execute(insert_query, data)

            # Commit the transaction if everything is successful
            self.conn.commit()

        except Exception as e:
            # Handle the exception
            print("Error:", e)
            
            # Rollback the transaction to start fresh
            self.cure.execute("ROLLBACK;")
