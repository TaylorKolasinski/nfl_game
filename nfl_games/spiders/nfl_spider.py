import scrapy
from scrapy.http import Request
from nfl_games.items import NflGamesItem
import json

class NflSpider(scrapy.Spider):
  name = 'nfl'
  allowed_domains = ["pro-football-reference.com"]
  start_urls = ['http://www.pro-football-reference.com/boxscores/']

  urls = []

  quarter_data = {'first': [], 'second': [], 'third': [], 'fourth': [], 'final': []}

  item = NflGamesItem()
  item['first_q'] = []
  item['second_q'] = []
  item['third_q'] = []
  item['fourth_q'] = []

  def parse(self, response):
    top_table = response.xpath("//table")[0]

    for i, row in enumerate(top_table.xpath('tr')):
      cols = row.xpath('td')
      for col in cols:
        text = col.xpath('a/text()').extract()
        if len(text) > 0:
          num = int(text[0].encode('utf-8'))
          if num >= 2000:
            url = 'http://www.pro-football-reference.com/years/' + text[0].encode('utf-8') + '/games.htm'
            request = Request(url, callback=self.open_year)
            
            yield request

  def open_year(self, response):
    table = response.xpath('//table')[0]
    cols  = table.xpath("tbody/tr[@class='']")

    for col in cols:
      boxscore = col.xpath('td')[3]
      if len(boxscore.xpath('a/@href').extract()) > 0:
        href = boxscore.xpath('a/@href').extract()[0].encode('utf-8')
        url = 'http://www.pro-football-reference.com' + href 
        request = Request(url, callback=self.open_boxscore)
 
        yield request
      
  def open_boxscore(self, response):
    table = response.xpath("//table")[1]
    # item = response.meta['item']

    first = []
    sec = []
    third = []
    four = []

    for row in table.xpath('tr'):
      if len(row.xpath('td/text()').extract()) > 1:
        fq = (int(row.xpath('td/text()').extract()[1].encode('utf-8'))) % 10
        sq = (int(row.xpath('td/text()').extract()[2].encode('utf-8')) + fq) % 10
        tq = (int(row.xpath('td/text()').extract()[3].encode('utf-8')) + sq) % 10
        foq = (int(row.xpath('td/text()').extract()[4].encode('utf-8')) + tq) % 10

        first.append(fq)
        sec.append(sq)
        third.append(tq)
        four.append(foq)
    
        self.item['first_q'] = first
        self.item['second_q'] = sec
        self.item['third_q'] = third
        self.item['fourth_q'] = four
    yield self.item

  # def legion_of_boom(self, response):
    
   # self.quarter_data['second_q'].append(sq)
      # self.quarter_data['third_q'].append(tq)
      # self.quarter_data['fourth_q'].append(foq)

      # item = {'first_q': item['first_q'], 'second_q': item['second_q'], 'third_q': item['third_q'], 'fourth_q': item['fourth_q']}

    # self.quarter_data['final'].append(final)

     # item['final'] = int(row.xpath('td/text()').extract()[5].encode('utf-8'))
        # self.item['first_q'].append(fq)
        # self.item['second_q'].append(sq)
        # self.item['third_q'].append(tq)
        # self.item['fourth_q'].append(foq)

        # self.quarter_data['first_q'].append(fq)
    
    # self.item['first_q'].append(first)
    # self.item['second_q'].append(sec)
    # self.item['third_q'].append(third)
    # self.item['fourth_q'].append(four)

           
    
         

