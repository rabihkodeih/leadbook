# -*- coding: utf-8 -*-
import json
import scrapy
from leadbook.constants import DATA_NO_VALUE


class CompanyProfilesSpider(scrapy.Spider):
    name = 'campany_profiles'
    custom_settings = {
        'ITEM_PIPELINES': {
            'leadbook.pipelines.CompanyProfilesItemVerificationPipeline': 100,
            'leadbook.pipelines.CrawlTimeAnnotatotionPipeline': 200
        }
    }

    def __init__(self, *args, **kwargs):
        self.root_url = 'https://www.idx.co.id/umbraco/Surface/ListedCompany/GetCompanyProfilesDetail/'
        self.yielded_items = 0
        self.total_items = 0
        self.input_file = kwargs.get('input_file')
        return super().__init__(*args, **kwargs)

    def start_requests(self):
        '''
        This is the starting point of the spider where all the starting urls
        are read from input and crawled through.
        '''
        if not self.input_file:
            raise Exception("Missing input_file argument")
        with open(self.input_file) as json_file:
            json_data = json_file.read()
            companies = json.loads(json_data)
            self.total_items = len(companies)
            for company in companies:
                ticker_symbol = company['ticker_symbol']
                url = '%s?kodeEmiten=%s' % (self.root_url, ticker_symbol)
                self.logger.info('Queued crawling at "%s"' % url)
                yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        '''
        Parses company item from response.
        '''
        row = json.loads(response.text)
        self.yielded_items += 1
        self.logger.info('items yielded: %s of %s' % (self.yielded_items, self.total_items))
        no_value = DATA_NO_VALUE
        profiles = row.get('Profiles', [{}])[0]
        item = {
            'company_name': profiles.get('NamaEmiten', no_value),
            'security_code': profiles.get('KodeEmiten', no_value),
            'office_address': profiles.get('Alamat', no_value),
            'email_address': profiles.get('Email', no_value),
            'country': profiles.get('Country', 'Indonesia'),
            'phone': profiles.get('Telepon', no_value),
            'fax': profiles.get('Fax', no_value),
            'npwp': profiles.get('NPWP', no_value),
            'company_website': profiles.get('Website', no_value),
            'ipo_date': profiles.get('TanggalPencatatan', no_value)[:10],
            'board': profiles.get('PapanPencatatan', no_value),
            'sector': profiles.get('Sektor', no_value),
            'sub_sector': profiles.get('SubSektor', no_value),
            'registrar': profiles.get('BAE', no_value),
            'corporate_secretary': [],
            'director': [],
            'subsidiary': []
        }
        # parse secretary data
        secretaries = row.get('Sekretaris', [])
        for secretary in secretaries:
            sec_item = {'name': secretary.get('Nama', no_value),
                        'email': secretary.get('Email', no_value),
                        'phone': secretary.get('Telepon', no_value)}
            item['corporate_secretary'].append(sec_item)
        # parse director data
        directors = row.get('Direktur', [])
        for director in directors:
            dir_item = {'name': director.get('Nama', no_value),
                        'position': director.get('Jabatan', no_value)}
            item['director'].append(dir_item)
        subsidiaries = row.get('AnakPerusahaan', [])
        # parse subsidiary data
        for subsidiary in subsidiaries:
            sub_item = {'name': subsidiary.get('Nama', no_value),
                        'type': subsidiary.get('BidangUsaha', no_value),
                        'total_asset': subsidiary.get('JumlahAset', no_value),
                        'percentage': subsidiary.get('Persentase', no_value)}
            item['subsidiary'].append(sub_item)
        yield item


# end of file
