import scrapy, time
from sciencedirect.items import SDparserItem
from scrapy_splash import SplashRequest
import re

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)



splash_url = 'http://localhost:8050/render.html?url='

class ArticleSpider(scrapy.Spider):
    name = "MC"
    # start_urls =[
    #     ,
    # ]
    def start_requests(self):
        yield SplashRequest(
            url=splash_url + 'https://www.sciencedirect.com/journal/mendeleev-communications/vol/29/issue/6',
            callback=self.parse,
        )

    def start_requests_articles(self):
        yield SplashRequest(
            url=splash_url + 'https://www.sciencedirect.com/science/article/pii/S0959943619302652',
            callback=self.parse,
        )

    def parse(self, response):

        vol_issue = remove_tags(response.css('h2.u-text-light.u-h1.js-vol-issue').extract_first())
        item_volume = vol_issue.split(',')[0].split(' ')[-1]
        item_issue = vol_issue.split(',')[1].split(' ')[-1]
        item_journal = response.css('span.anchor-text').extract_first()

        print(item_volume)
        print(item_issue)
        print(item_journal)



    def parse_authors(self, response):
        ''' Вытаскиваем даннын из строки вида Volume 29, Issue 6, November–December 2019, Pages 616-618'''

        # item_journal = remove_tags(response.css('a.publication-title-link').extract_first())
        # # print(journal)
        # item_volume = remove_tags(response.css('div.text-xs').extract_first()).split(',')[0].split(' ')[-1]
        # # print(volume)
        # item_issue = remove_tags(response.css('div.text-xs').extract_first()).split(',')[1].split(' ')[-1]
        # # print(issue)
        # item_year = remove_tags(response.css('div.text-xs').extract_first()).split(',')[2].split(' ')[-1]
        # # print(year)
        # item_pages = remove_tags(response.css('div.text-xs').extract_first()).split(',')[3].split(' ')[-1]
        # # print(pages)
        # item_name = remove_tags(response.css('h1').extract_first())
        # # print(name)
        item_authors = []
        authors = response.css('span.content').extract()
        for author in authors:
            item_authors.append(remove_tags(author))
        # # print(item_authors)
        # item_doi = response.css('a.doi::text').extract_first()[16:]
        # # print(doi)
        #
        # articleItem = SDparserItem(doi=item_doi, name=item_name, authors=item_authors, journal=item_journal,
        #                            year=item_year, volume=item_volume, issue=item_issue, pages=item_pages)
        # print('yield')
        # yield articleItem
        # nexturl = splash_url+'https://www.sciencedirect.com/sdfe/arp/issue/S0959943619X00073/article/S0959943619302652/siblings'

        # yield SplashRequest(url=nexturl, callback=self.parse_json)
        #
        # next_page = response.xpath('ul').extract()
        # print(next_page)
        # if next_page is not None:
        #     next_page = response.urljoin(splash_url+ next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)








