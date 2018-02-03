# -*- coding: utf-8 -*-
import scrapy


class ZvgPageSpider(scrapy.Spider):
    name = 'zvg-page'

    start_urls = [
        'http://www.zvg-online.net/1300/1106731773/ag_seite_001.php',
    ]

    def parse(self, response):
        for link in response.css('a.navi_term_vor'):
            yield {
                'href': link.xpath('@href').extract(),
            }
        yield {
            'title': response.selector.xpath('//title/text()').extract()
        }