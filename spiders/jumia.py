#Imports
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

from first.items import ProductItem


#Custom Spider Class
class JumiaSpider(CrawlSpider):
    name = 'jumia'
    allowed_domains = ['jumia.com.ng']
    start_urls = ['https://jumia.com.ng/groceries/']
    base_url =  'https://jumia.com.ng'

    
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='flyout']/a"),   callback='parse_product_details', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div/a[@class='pg'][5]"),   callback='parse_product_details', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div/a[@class = 'cbs'][3]"),   callback='parse_product_details', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div/a[@class='pg'][5]"),   callback='parse_product_details', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='core']"), callback='parse_product_details', follow=True),
    )


    def parse_product_details(self,response):
        exist = response.xpath("//h2[@class='-fs20 -m -phm -pvxs']").extract_first()
        loader= ItemLoader(item=ProductItem(),response=response)
        if exist:
            image = ''.join(response.xpath("//div[@id='imgs']/a/@href").extract_first())
            title = response.xpath("//div[@class = '-fs0 -pls -prl']/h1/text()").extract_first()
            final_title = re.sub('[^A-Za-z0-9.]+' , ' ', title)
            price = ''.join(response.xpath("//span[@class='-b -ltr -tal -fs24']/text()").extract_first())
            final_price = re.sub('[^A-Za-z0-9.]+' , ' ', price)
            description = ''.join(response.xpath("//div[@class='markup -mhm -pvl -oxa -sc']//text()").extract())
            final_description = re.sub('[^A-Za-z0-9.]+' , ' ', description).lower()
            feature = ''.join(response.xpath("//div[@class='markup -pam']/ul//text()").extract())
            final_feature = re.sub('[^A-Za-z0-9.]+' , ' ', feature)
            sku = ''.join(response.xpath("//li[@class='-pvxs'][1]//text()").getall())
            spec_2 = ''.join(response.xpath("//li[@class='-pvxs'][2]//text()").getall())
            spec_3 = ''.join(response.xpath("//li[@class='-pvxs'][3]//text()").getall())
            spec_4 = ''.join(response.xpath("//li[@class='-pvxs'][last()-1]//text()").getall())
            Weight = ''.join(response.xpath("//li[@class='-pvxs'][last()]//text()").getall())
            category = response.xpath("//div/a[@class = 'cbs'][2]/text()").extract_first()
            sub_category = response.xpath("//div/a[@class='cbs'][3]/text()").extract_first()
            sub_su_category =  response.xpath("//div/a[@class='cbs'][4]/text()").extract_first()

            yield {

                'image': image,
                'title': final_title,
                'price': final_price,
                'description': final_description,
                'features': final_feature,
                'sku': sku,
                'spec_2': spec_2,
                'spec_3': spec_3,
                'spec_4': spec_4,
                'Weight': Weight,
                'Weight': Weight,
                'category': category,
                'sub-category': sub_category,
                'sub-su-category':sub_su_category,

                'user-agent': response.request.headers.get('User-Agent').decode('utf-8')

            }
        else:
            print(response.url)
       

