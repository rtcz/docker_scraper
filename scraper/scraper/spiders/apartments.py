import os

import scrapy

from scraper.items import ApartmentItem


class ApartmentsSpider(scrapy.Spider):
    name = "apartments"
    allowed_domains = ["sreality.cz"]
    max_item_count = os.environ.get('MAX_ITEM_COUNT', 10)
    start_urls = [
        f"https://www.sreality.cz/api/en/v2/estates?"
        f"category_main_cb=1&"
        f"category_type_cb=1&"
        f"page=2&"
        f"per_page={max_item_count}"
    ]

    # noinspection PyMethodOverriding
    def parse(self, response) -> list[ApartmentItem]:
        data = response.json()
        result = []

        for estate in data['_embedded']['estates']:
            item = ApartmentItem()
            item['title'] = estate['name']
            item['locality'] = estate['locality']
            item['price'] = estate['price']
            images = estate['_links']['images']
            item['image_url'] = images[0]['href'] if images else None

            result.append(item)

        return result
