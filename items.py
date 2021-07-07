# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def remove_quotations(value):
    return value.replace(u"\u2019", '').replace(u"\u2013", '')

def strip_value(value):
    return value.strip()


class ProductItem(scrapy.Item):
    image= scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )

    final_title= scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )

    final_price= scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )

    final_description = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    final_feature = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    sku = scrapy.Field(
        input_processor= MapCompose(remove_quotations, strip_value),
        output_processor= TakeFirst()

    )

    spec_2 = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )

    spec_3 = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )

    spec_4 = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )

    Weight = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    
    category = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    

    sub_category = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    

    sub_su_category = scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    
    