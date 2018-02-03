# -*- coding: utf-8 -*-
import scrapy


class DetailsPageSpider(scrapy.Spider):
    name = "details-page"

    start_urls = [
        'http://www.zvg-online.net/1300/1106731773/termin_0001.php',
    ]

    def parse(self, response):
        yield {
            'sellDate': response.xpath('//nobr/b[1]/text()').extract_first(),
            'sign':  response.xpath('//td').re_first(r'[0-9]+\s[A-Z]\s[0-9]+/[0-9]+'),
            'type': response.xpath("//td[text()='Grundstücksart:']/following-sibling::td/text()").extract_first(),
            'address': response.xpath("//td[text()='Objekt / Lage:']/following-sibling::td/text()").extract_first(),
            'coordinates': response.xpath("//a/@href").re_first(r".*term_map\.php\?(.*)"),
            'price': response.xpath("//p").re_first(r"[0-9]+\.[0-9]+,[0-9]+"),
            'url': response.request.url
        }
