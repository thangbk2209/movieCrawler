import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
typeMovies = ["phim-co-trang/", 'phim-hai/','phim-tam-ly/','phim-tinh-cam-lang-man/',
                'phim-tai-lieu/','phim-vien-tuong/','phim-phieu-luu/','phim-kinh-di/','phim-hanh-dong/']
start_urls=[]
for movie in typeMovies:
    urli = 'http://www.phimmoi.net/the-loai/'+ movie
    start_urls.append(urli)
class BrickSetSpider(scrapy.Spider):
    name = "spider"
    def start_requests(self):
        for url in start_urls: 
            print 'loli',url
            yield scrapy.Request(url = url, callback = self.parse)
    def parse(self, response):
        linkMovies = []
        linkBackgrounds = []
        movieTitles=response.css('span.movie-title-1::text').extract()
        movieEngTitles=response.css('span.movie-title-2::text').extract()
        print len(movieTitles)
        print len(movieEngTitles)
        for i in range(27):
            linkMovieXPath = '//*[@class="movie-list-index"]/ul/li[' + str(i+1) + "]/a/@href"
            linkBackgroundXpath = '//*[@class="movie-list-index"]/ul/li[' + str(i+1) + "]/a/div/@style"
            linkMovies.append(response.xpath(linkMovieXPath).extract_first())
            linkBackgrounds.append(response.xpath(linkBackgroundXpath).extract_first())
            print linkMovies
            print 'linkMovies'
        print len(linkMovies)
        if (movieTitles):
            for i in range(len(movieTitles)):
                yield{
                    'category': movie ,
                    'linkMovie':'http://www.phimmoi.net/'+ linkMovies[i],
                    'linkBackground':linkBackgrounds[i].split(')')[0].split('(')[1],
                    'title':movieTitles[i],
                    'engTitle': movieEngTitles[i]
                }
        # print 'questions'
        # print questions
        # filename = 'check.txt'
        # with open(filename, 'wb') as f:
        #     f.write(questions)
        # self.log('Saved file %s' % filename)