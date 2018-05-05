import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

import json
with open('data/data.json') as f:
    phim = json.load(f)
print phim['movie'][0]['linkPhim']
movieList = phim['movie']
movieLinkList = []
print len(movieList)
for i in range(len(movieList)):
    print movieList[i]
    linki = movieList[i]['linkPhim']
    movieLinkList.append(linki)
print len(movieLinkList)
class BrickSetSpider(scrapy.Spider):
    name = "movieInfo"
    def start_requests(self):
        i = 0
        for url in movieLinkList: 
            i+=1
            print 'loli',url
            yield scrapy.Request(url = url, callback = self.parse)
        print 'i',i
    def parse(self, response):
        countryInfo=response.css('a.country::text').extract()
        title = response.css('a.title-1::text').extract()
        year = response.xpath('//*[@class="movie-meta-info"]/dl/dd[4]/a/text()').extract_first()
        # for i in range(27):
        #     linkXPath = '//*[@class="movie-list-index"]/ul/li[' + str(i+2) + "]/a"
        # year = response.xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/dl/dd[4]/a').extract_first()
        #     print self_titles
        #     print 'self_title'
        #     for i in range(len(movieTitles)):
        # print 'title i ', title
        if(len(year)==4):
            yield{
                'title': title[0],
                'country':countryInfo[0],
                'year':year,
                'imdb': 'null'
            }
        else:
            year = response.xpath('//*[@class="movie-meta-info"]/dl/dd[6]/a/text()').extract_first()
            imdb = response.css('dd.imdb::text').extract()
            if(year != null):
                yield{
                    'title': title[0],
                    'country':countryInfo[0],
                    'year':year,
                    'imdb': imdb
                }
            else:
                year = response.xpath('//*[@class="movie-meta-info"]/dl/dd[5]/a/text()').extract_first()
                yield{
                    'title': title[0],
                    'country':countryInfo[0],
                    'year':year,
                    'imdb': imdb
                }
        # print 'questions'
        # print questions
        # filename = 'check.txt'
        # with open(filename, 'wb') as f:
        #     f.write(questions)
        # self.log('Saved file %s' % filename)