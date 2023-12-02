import scrapy
import json
import re
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
import csv
from sreality.items import SrealityItem


class SrealityflatsSpider(scrapy.Spider):
    name = "SrealityFlats"
    allowed_domains = ["www.sreality.cz"]
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response):
        sreality_item = SrealityItem()
        response_json = json.loads(response.body)
        for flat in response_json.get('_embedded').get('estates'):
            
            sreality_item['title'] = re.sub(r'\s', ' ', flat.get('name'))
            sreality_item['image_url'] = flat.get('_links').get('images')[0].get('href')

            yield sreality_item
            

def sreality_flat_spider_result():
    flats_results = []

    def crawler_results(item):
        flats_results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(SrealityflatsSpider)
    crawler_process.start()

    return flats_results


if __name__ == '__main__':
    
    flats_data=sreality_flat_spider_result()

    # Debug csv data exporter
    #keys = flats_data[0].keys()
    #with open('flats_data.csv', 'w', newline='') as output_file_name:
    #    writer = csv.DictWriter(output_file_name, keys)
    #    writer.writeheader()
    #    writer.writerows(flats_data)