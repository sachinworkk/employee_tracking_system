import scrapy
from urllib.parse import urlencode

import os
from dotenv import load_dotenv


load_dotenv()

def get_proxy_url(url):
    payload = {'api_key':os.environ.get("API_KEY"), 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class Linkedin(scrapy.Spider):
    name = 'linkedin'

    # These are the urls that we will start scraping
    def start_requests(self):
        urls = [
           'https://np.linkedin.com/in/pooja-bajracharya-66721489',
        #    'https://np.linkedin.com/in/prakash-aryal-20ab317',
        #    'https://np.linkedin.com/in/krishnadhakal',
        ]

        for url in urls:
            yield scrapy.Request(url=get_proxy_url(url), callback=self.parse)
       

    def parse(self,response):
        title = response.css('title').extract()
        yield{'titletext': title}

   