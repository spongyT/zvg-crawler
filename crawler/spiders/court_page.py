# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin


class CourtPageSpider(scrapy.Spider):
    name = 'court-page'

    start_urls = [
        'http://www.zvg-online.net/1300/1106731773/ag_seite_001.php',
    ]

    def parse(self, response):
        # print(">>>>>", response.request.url, response.request.url.rfind("/"))
        # base = response.request.url[0:response.request.url.rfind("/")+1]
        # print(">>>>>", base)
        # for relative_link in response.xpath("//a/@href").re(r"termin_[0-9]+\.php"):
        #     yield urljoin(base, ''.join(relative_link))
        yield {
            "links": response.xpath("//a/@href").re(r"termin_[0-9]+\.php")
        }