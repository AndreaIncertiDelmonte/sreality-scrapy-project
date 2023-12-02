# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import os

class PostgresSrealityPipeline:

    def __init__(self):

        ## Connection details from ENV variables
        hostname = os.getenv("POSTGRES_HOST", "127.0.0.1")
        username = os.getenv("POSTGRES_USER", "default_pg_user")
        password = os.getenv("POSTGRES_PASSWORD", "default_pg_password")
        database = os.getenv("POSTGRES_DB", "default_pg_db")
        port = os.getenv("POSTGRES_HOST_PORT", "5432")

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        # Delete table
        self.cur.execute("""
        DROP TABLE IF EXISTS flats 
        """)

        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flats (
            id serial PRIMARY KEY, 
            title text,
            image_url text
        )
        """)
        
    def process_item(self, item, spider):

        self.cur.execute(""" insert into flats (title, image_url) values (%s,%s)""", (
            item["title"],            
            item["image_url"]
        ))

        self.connection.commit()
        
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()