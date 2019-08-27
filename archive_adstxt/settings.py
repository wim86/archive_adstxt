# -*- coding: utf-8 -*-

# Scrapy settings for archive_adstxt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'archive_adstxt'

SPIDER_MODULES = ['archive_adstxt.spiders']
NEWSPIDER_MODULE = 'archive_adstxt.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'archive_adstxt.pipelines.ArchiveAdstxtPipeline': 300,
}


DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 610}
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = ''
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600