import scrapy


class ApartmentItem(scrapy.Item):
    title: str = scrapy.Field()
    image_url: str = scrapy.Field()
    locality: str = scrapy.Field()
    price: int = scrapy.Field()
