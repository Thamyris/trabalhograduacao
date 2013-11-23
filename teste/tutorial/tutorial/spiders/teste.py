from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import pymongo
from tutorial.items import DmozItem 

class workSpider(BaseSpider):
      
    name = "work"
    start_urls = ["http://vagas.infojobs.com.br/vagas-empregos-.aspx"]

    def parse(self, response):
        
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('..//div[@class=" orddata"]/ul')
        items = []
        f = open('texto.txt', 'w')
        for site in sites:
            item = DmozItem()
            item['titleVaga'] = ''.join(site.select('li//h2/text()').extract())
            item['link'] = ''.join(site.select('li/a[@class="vagaTitle"]/@href').extract())
            item['desc'] = ''.join(site.select('li[@class="vagaDesc"]/text()').extract())
            item['location'] = ''.join(site.select('li[@class="location2"]/text()').extract())
            item['area'] = ''.join(site.select('li[@class="area "]/span/text()').extract())
            items.append(item)

            #print('\n\n\n\n++++++++')
            #print('\n\n\n\n++++++++')
            f.write(', '.join(item.values()).encode('utf-8'))
        f.close()
        return items



## filename = response.url.split("/")[-2]
        ##open(filename,'wb').write(response.body)

 # title = site.select('a/text()').extract()
           # link = site.select('a/@href').extract()
            #desc = site.select('text()').extract()
            #print (title, link, desc)

