#-*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import pymongo
from unicodedata import normalize
#from tutorial.items import DmozItem

#def remover_acentos(txt, codif='utf-8'):
#     return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')# http://www.python.org.br/wiki/RemovedorDeAcentos  

def remover_acentos(txt):
     return normalize('NFKD', txt).encode('ascii','ignore').replace('\r\n', '').strip()

class workSpider(BaseSpider):
    name = "work2"
    start_urls = ["http://vagas..com.br/vagas-empregos-.aspx"]
    

    def parse(self, response):
        conn = pymongo.Connection('localhost')
        db = conn.bancoTesteEmpregoInfoJobs
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('..//div[@class=" orddata"]/ul')
        #items = []
        #f = open('texto.txt', 'w')
        for site in sites:
           # frase_normal = remover_acento
            #item = DmozItem()
            location = (site.select('li[@class="location2"]/text()').extract())
            for local in location :
                cidade,estado = local.split('-')
                vagaS1 = {'titleVaga' : remover_acentos(' - '.join(site.select('li//h2/text()').extract())),
                          'link' : (site.select('li/a[@class="vagaTitle"]/@href').extract()),
                          'desc' : remover_acentos(' - '.join(site.select('li[@class="vagaDesc"]/text()').extract())),
                          'cidade' : remover_acentos(cidade),
                          'estado' : remover_acentos(estado),
                          'area'  : remover_acentos(' - '.join(site.select('li[@class="area "]/span/text()').extract()))
                         }
            vaga = db.vaga
            vaga_id = vaga.insert(vagaS1)
            
            
           # items.append(item)
           
            #print('\n\n\n\n++++++++')
            #print('\n\n\n\n++++++++')
           # f.write(', '.join(item.values()).encode('utf-8'))
        #f.close()
        



## filename = response.url.split("/")[-2]
        ##open(filename,'wb').write(response.body)

 # title = site.select('a/text()').extract()
           # link = site.select('a/@href').extract()
            #desc = site.select('text()').extract()
            #print (title, link, desc)
