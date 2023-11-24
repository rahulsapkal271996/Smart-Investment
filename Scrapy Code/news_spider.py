import scrapy

class QuoteSpider(scrapy.Spider):
	name="news"
	start_urls=['https://www.coindesk.com']

	def parse(self,response):
		for quote in response.css('div'):
			yield{
				'News': quote.xpath('div/h3/a/text()').extract_first(),
				'Date':quote.xpath('div/p/time/text()').extract_first()

			}
		next_page=''
		for i in range(2,500):
			next_page='https://www.coindesk.com/page/' + str(i)+'/'
			yield scrapy.Request(next_page,callback=self.parse)
			