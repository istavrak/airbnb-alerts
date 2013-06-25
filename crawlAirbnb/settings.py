# Scrapy settings for crawlAirbnb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawlAirbnb'

SPIDER_MODULES = ['crawlAirbnb.spiders']
NEWSPIDER_MODULE = 'crawlAirbnb.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawlAirbnb (+http://www.yourdomain.com)'
