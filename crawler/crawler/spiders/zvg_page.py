# -*- coding: utf-8 -*-
import scrapy


class ZvgPageSpider(scrapy.Spider):
    name = 'zvg-page'

    start_urls = [
        'http://www.zvg-online.net/1300/1106731773/ag_seite_001.php',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'output/%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
