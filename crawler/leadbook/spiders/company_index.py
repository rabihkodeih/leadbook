# -*- coding: utf-8 -*-
import json
import scrapy


class CompanyIndexSpider(scrapy.Spider):
    name = 'campany_index'
    custom_settings = {
        'ITEM_PIPELINES': {
            'leadbook.pipelines.CompanyIndexItemVerificationPipeline': 100,
            'leadbook.pipelines.CrawlTimeAnnotatotionPipeline': 200
        }
    }

    def __init__(self, *args, **kwargs):
        self.root_url = 'https://www.idx.co.id/umbraco/Surface/ListedCompany/GetCompanyProfiles'
        self.length = 10
        self.yielded_items = 0
        self.total_items = 0
        return super().__init__(*args, **kwargs)

    def start_requests(self):
        '''
        This is the starting point of the spider where all the starting urls
        are read from input and crawled through.
        '''
        start_url = '%s?start=0&length=%s' % (self.root_url, self.length)
        yield scrapy.Request(url=start_url, callback=self.process_main_response)

    def process_main_response(self, response):
        '''
        Processes main response from the root url. ALl items are first extracted
        then remaining results are queued and subsequently parsed.
        '''
        data = json.loads(response.text)
        self.total_items = data.get('recordsTotal', 0)
        yield from self.parse_items(response)
        for start in range(self.length, self.total_items, self.length):
            url = '%s?start=%s&length=%s' % (self.root_url, start, self.length)
            self.logger.info('Queued crawling at "%s"' % url)
            yield scrapy.Request(url=url, callback=self.parse_items)

    def parse_items(self, response):
        '''
        Parses all items in a results response.
        '''
        all_data = json.loads(response.text)
        rows = all_data.get('data')
        for row in rows:
            self.yielded_items += 1
            self.logger.info('items yielded: %s of %s' % (self.yielded_items, self.total_items))
            yield self.item_from_row(row)

    def item_from_row(self, row):
        '''
        Extracts item from row json data.
        '''
        url_base = 'http://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/'
        no_value = ''
        item = {
            "ticker_symbol": row.get('KodeEmiten', no_value),
            "company_name": row.get('NamaEmiten', no_value),
            "url": '%s?kodeEmiten=%s' % (url_base, row.get('KodeEmiten', no_value)),
            "listing_date": row.get("TanggalPencatatan", no_value)[:10],
        }
        return item


# end of file
