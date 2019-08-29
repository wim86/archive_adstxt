
from scrapy.spiders import Spider
from scrapy import Request

from archive_adstxt.items import ArchiveAdstxtItem, ArchiveAdstxtItemLoader
from urllib.parse import urlencode

import json
import logging
import csv


class ArchiveSpider(Spider):
    name = 'archive'

    allowed_domains = ['web.archive.org', ]
    start_urls = ['https://web.archive.org/']
    maximum_reviews = 20

    def __init__(self, input_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_file = input_file

    def start_requests(self):
        search_url = "https://web.archive.org/__wb/sparkline?"
        list_domains = set()
        with open(self.input_file) as domains_file:
            reader = csv.reader(domains_file)
            next(reader)
            for row in reader:
                logging.debug(f"row is {row}")
                #split_row = row[0].split(',')
                domain = row[0]
                try:
                    direct = row[3]
                except IndexError:
                    direct = 'DIRECT'
                if direct == 'DIRECT' and domain not in list_domains:
                    list_domains.add(domain)
                    query = {'url': domain.strip() + '/ads.txt',
                             'collection': 'web',
                             'output': 'json'}
                    yield Request(search_url + urlencode(query),
                                  callback=self.parse_search,
                                  meta={'domain': domain})
                    logging.info(f"{domain}")

    def parse_search(self, response):
        result = json.loads(response.text)
        last_ts = result['last_ts']
        domain = response.meta['domain']
        if last_ts:
            logging.debug(f"Found for domain {domain}")
            loader = ArchiveAdstxtItemLoader(
                item=ArchiveAdstxtItem(), response=response)
            loader.add_value('domain', domain)
            item = loader.load_item()
            yield item
        else:
            logging.debug(f"Not found for domain {domain}")