# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class JobscraperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(Item):
    title = Field()
    company = Field()
    salary = Field()
    location = Field()
    date = Field()
    img = Field()
    source = Field()
    