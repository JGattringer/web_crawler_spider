#lets import the framework and spider func
from scrapy import Spider, Request

#create a class and pass the spider as a parameter
class Web_scrapy(Spider):
    name = "Ultima Online"
    start_urls = ["https://pt.wikipedia.org/wiki/Ultima_Online"]

# create a parse function to get a response
    def parse(self, response):
        for quote in response.css("div.quote"):  # make a loop for every quote
            yield {
                "text": quote.css("span.text::text").extract(),
                "autor": quote.css("small.author::text").extract(),
                "tags": quote.css("div.tags a.tag::text").extract()
            }
        links = response.css("a.mw-redirect::attr(href)").extract()
        for link in links:
            yield Request(response.urljoin(link), callback=self.parse_secondary)

    def parse_secondary(self, response):
        # extrac the data from secondary pages
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract(),
                "autor": quote.css("small.author::text").extract(),
                "tags": quote.css("div.tags a.tag::text").extract()
            }
