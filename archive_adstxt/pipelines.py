# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class ArchiveAdstxtPipeline(object):
    def __init__(self):
        self.writer = None
        self.file = None

    def open_spider(self, spider):
        filename = "test_output.csv"
        self.file = open(filename, 'w')
        self.writer = csv.writer(self.file)
        self.writer.writerow(["domain"])

    def process_item(self, item, spider):
        domain = item['domain']
        self.writer.writerow([domain])
        return item

    def close_spider(self, spider):
        self.file.close()
