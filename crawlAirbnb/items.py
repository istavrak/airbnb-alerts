# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class apartment_Item(Item):
    image_URI=Field()
    room_id=Field()
    room_title=Field()
    room_price=Field()
    host_id=Field()
    room_URI=Field()
