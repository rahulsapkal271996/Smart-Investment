import scrapy

class QuoteSpider(scrapy.Spider):
	name="btc_data"
	start_urls=['https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130428&end=20180214']

	def parse(self,response):
		for quote in response.css('tr'):
			yield{
				'Date': quote.xpath('td/text()').extract_first(),
				'Open': quote.css('tr td:nth-child(2)::text').extract(),
				'High': quote.css('tr td:nth-child(3)::text').extract(),
				'Low': quote.css('tr td:nth-child(4)::text').extract(),
				'Close': quote.css('tr td:nth-child(5)::text').extract(),
				'Volume': quote.css('tr td:nth-child(6)::text').extract(),
				'Market Cap': quote.css('tr td:nth-child(7)::text').extract(),
				'Name':'Ethereum'
			}
		# next_page=response.css('div.pagination li.next a::attr("href")').extract_first()
		# if next_page <> '/newstopics/cryptocurrency/page-8/':
			# next_page=response.urljoin(next_page)
			# yield scrapy.Request(next_page,callback=self.parse)
		# else:
			# raise CloseSpider('Scraped Data')
	