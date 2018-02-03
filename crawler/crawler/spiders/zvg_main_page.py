# -*- coding: utf-8 -*-
import scrapy


class ZvgMainPageSpider(scrapy.Spider):
    name = "zvg_main_page"

    start_urls = [
        'http://www.zvg-online.net/1300/index.php',
    ]

    def parse(self, response):
        response.css('navi').extract()
        # for link in response.css('navi'):
        #     yield {
        #         'href': link.xpatch('@href').extract(),
                # 'name': link.xpatch('/text()').extract(),
            # }
