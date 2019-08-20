# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Identity, TakeFirst


class ArchiveAdstxtItemLoader(scrapy.loader.ItemLoader):
    default_input_processor = Identity()
    default_output_processor = TakeFirst()


class ArchiveAdstxtItem(scrapy.Item):
    domain = scrapy.Field()
    pass
