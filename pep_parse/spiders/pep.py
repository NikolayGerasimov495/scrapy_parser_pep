import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (ALLOWED_DOMAINS, NAME, PEP_STATUS_SELECTOR,
                                START_URLS)


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):

        all_links_pep = response.css('td:nth-child(2) a::attr(href)').getall()

        for link_pep in all_links_pep:
            yield response.follow(link_pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        if title:
            title_parts = title.split(' – ')
            if len(title_parts) == 2:
                number, name = title_parts[0].strip(), title_parts[1].strip()
            else:
                self.logger.warning(
                    f"Не удалось распарсить заголовок: {title}")
                return

            status = response.css(PEP_STATUS_SELECTOR).get()
            yield PepParseItem(number=number, name=name, status=status)
        else:
            self.logger.warning("Не найден заголовок страницы PEP.")
