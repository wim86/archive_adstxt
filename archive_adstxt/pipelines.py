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
        self.filename = None
        self.counter = 0

    def open_spider(self, spider):
        self.filename = "test_output.csv"
        self.file = open(self.filename + '_' + str(self.counter), 'w')
        self.writer = csv.writer(self.file)
        self.writer.writerow(["domain"])

    def process_item(self, item, spider):
        self.counter += 1
        domain = item['domain']
        self.writer.writerow([domain])
        if self.counter % 5000 == 0:
            self.file.close()
            self.file = open(self.filename + '_' + str(self.counter), 'w')
        return item

    def close_spider(self, spider):
        self.file.close()
