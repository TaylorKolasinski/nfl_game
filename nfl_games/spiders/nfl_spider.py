import scrapy
from scrapy.http import Request
from nfl_games.items import NflGamesItem

class NflSpider(scrapy.Spider):
  name = 'nfl'
  allowed_domains = ["pro-football-reference.com"]
  start_urls = ['http://www.pro-football-reference.com/boxscores/']

  def parse(self, response):
    top_table = response.xpath("//table")[0]
    for row in top_table.xpath('tr'):
      cols = row.xpath('td')
      for col in cols:
        text = col.xpath('a/text()').extract()
        if len(text) > 0:
          num = int(text[0].encode('utf-8'))
          if num >= 1970:
            url = 'http://www.pro-football-reference.com/years/' + text[0].encode('utf-8') + '/games.htm'
            request = Request(url, callback=self.open_year)

            yield request

  def open_year(self, response):
    table = response.xpath('//table')[0]
    col = table.xpath('tbody/tr/td')[3]
    href = col.xpath('a/@href').extract()[0].encode('utf-8')

    url = 'http://www.pro-football-reference.com' + href 

    request = Request(url, callback=self.open_boxscore)

    yield request
    

  def open_boxscore(self, response):
    table = response.xpath("table[@class='stats_table']")

    rows = table.xpath('tr')

    print rows
         

