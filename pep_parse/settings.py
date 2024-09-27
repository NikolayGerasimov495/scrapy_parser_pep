import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOT_NAME = "pep_parse"

NAME = 'pep'

ALLOWED_DOMAINS = ['peps.python.org']

START_URLS = ["https://peps.python.org/"]

PEP_STATUS_SELECTOR = '#pep-content > dl > dd abbr::text'

SPIDER_MODULES = ["pep_parse.spiders"]

NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
