'''
Created on Jun 23, 2013

@author: istavrak
'''
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from crawlAirbnb.items import apartment_Item
import MySQLdb as mdb
import ConfigParser


class gpspider(BaseSpider):
    name="abHotelsList"
    allowed_domains=["airbnb.com"]
    
    Config = ConfigParser.ConfigParser()
    Config.read("..//settings.cfg")
    db_user=Config.get("MYSQL", "db_user")
    db_pass=Config.get("MYSQL", "db_pass")
    db_location=Config.get("MYSQL", "db_location")
    db_name=Config.get("MYSQL", "db_name")
    search_url=Config.get("Scrapy", "search_url")
    
    start_urls=[search_url]
    
   
    
    def parse(self,response):
        
        con = mdb.connect(self.db_location, self.db_user, self.db_pass, self.db_name);
        classResultItem='search_result ' #div - wraps the result item
        classRoomImage='pop_image_small' #div - wraps the URI to the image of the room
        classRoomPriceWraper='price monthly' #h3 - wraps the title of the room
        classRoomPrice='price_data' #h3 - wraps the title of the room
        
        
        hxs=HtmlXPathSelector(response)
        
        next_page =hxs.select("//div[@class='pagination']//li[@class='next next_page']/a/@href").extract()
        #print(next_page)
        if not not next_page:
            yield Request("https://www.airbnb.com/"+next_page[0], self.parse)


        #pagination_counter=int(float(str(pagination.select('count(.//li)').extract()[0])))-1
        
        results=hxs.select('//li[@class="'+classResultItem+'"]')
        rooms=[]
        #print(len(results))
        for result in results:
            ritem_hxs=result
            room_item=apartment_Item()

            room_item['room_id']=ritem_hxs.select('@data-hosting-id').extract()[0]
            room_item['host_id']=ritem_hxs.select('@data-host-id').extract()[0]
            room_item['room_URI']='https://www.airbnb.com/rooms/'+room_item['room_id']
            room_item['room_title']=ritem_hxs.select('.//div[@class="'+classRoomImage+'"]/a').select('@title').extract()[0]
            room_item['room_price']=float(str(ritem_hxs.select('.//div[@class="'+classRoomPriceWraper+'"]/div[@class="'+classRoomPrice+'"]').select('text()').extract()[1]))
            room_item['image_URI']=ritem_hxs.select('.//div[@class="'+classRoomImage+'"]/a/img').select('@data-original').extract()[0]
            
            rooms.append(room_item)
            
            
        with con:        
            for item in rooms:
                cur = con.cursor()
                cur.execute('INSERT IGNORE INTO entries(room_id,host_id,room_title,room_price,image_uri,room_URI,status) VALUES(%s,%s,%s,%s,%s,%s,NOW())',[item['room_id'],item['host_id'],item['room_title'],item['room_price'],item['image_URI'],item['room_URI']])
        #    yield item
