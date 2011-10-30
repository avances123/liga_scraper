from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from liga_scraper.items import LigaScraperItem

class DmozSpider(BaseSpider):
	name = "ligayahoo"
	allowed_domains = ["http://es.laliga.fantasysports.yahoo.com"]
	start_urls = ["http://es.laliga.fantasysports.yahoo.com/football/62094/topplayers?sort_by=points&position=F&week=&season=2011"]

	def parse(self, response):
		items = []
		hxs = HtmlXPathSelector(response)
		players = hxs.select('//div[1]/div/div[2]/table/tbody/tr[td]')
		for player in players:
			item = LigaScraperItem()
			item['posicion'] = player.select('//div[1]/div/div[2]/table/tbody/tr[td]/*[4]/text()').extract()
			item['jugador'] = hxs.select('//div[1]/div/div[2]/table/tbody/tr[td]/*[2]/a/text()').extract()
			item['equipo'] = hxs.select('//div[1]/div/div[2]/table/tbody/tr[td]/*[3]/text()').extract()
			item['precio_mercado'] = hxs.select('//div[1]/div/div[2]/table/tbody/tr[td]/*[5]/text()').extract()
			item['puntos'] = hxs.select('//div[1]/div/div[2]/table/tbody/tr[td]/*[6]/text()').extract()
			items.append(item)
		
		return items

		#print posicion,jugador,equipo,precio_mercado,puntos
		#print 

		#filename = response.url.split("/")[-2]
		#open(filename, 'wb').write(response.body)


