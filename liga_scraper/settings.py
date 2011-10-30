# Scrapy settings for liga_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'liga_scraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['liga_scraper.spiders']
NEWSPIDER_MODULE = 'liga_scraper.spiders'
DEFAULT_ITEM_CLASS = 'liga_scraper.items.LigaScraperItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

