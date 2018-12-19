# -*- coding: utf-8 -*-

from datetime import datetime
from leadbook.utils import validate_fields


class CompanyIndexItemVerificationPipeline(object):
    '''
    This pipeline verifies all fields of every parsed item. Verification
    happens based on a given list of (field, regex-validator) tuple.
    If verification fails, the item is dropped and an appropriate
    log message is issued.
    '''
    def process_item(self, item, spider):
        fields = [('ticker_symbol', '^[A-Z][A-Z][A-Z][A-Z]$'),
                  ('company_name', '^.+$'),
                  ('listing_date', '^\d\d\d\d-\d\d-\d\d$')]
        validate_fields(item, fields, spider, check_null_values=True)
        return item


class CompanyProfilesItemVerificationPipeline(object):
    '''
    This pipeline verifies all fields of every parsed item. Verification
    happens based on a given list of (field, regex-validator) tuple.
    If verification fails, the item is dropped and an appropriate
    log message is issued.
    '''
    def process_item(self, item, spider):
        fields = [('company_name', '^.+$'),
                  ('security_code', '^[A-Z][A-Z][A-Z][A-Z]$'),
                  ('office_address', '^.+$'),
                  ('email_address', '^.+$'),
                  ('phone', '^.+$'),
                  ('fax', '^.+$'),
                  ('npwp', '^.+$'),
                  ('company_website', '^.+$'),
                  ('ipo_date', '^\d\d\d\d-\d\d-\d\d$'),
                  ('board', '^.+$'),
                  ('sector', '^.+$'),
                  ('sub_sector', '^.+$'),
                  ('registrar', '^.+$')]
        validate_fields(item, fields, spider, check_null_values=True)
        return item


class CrawlTimeAnnotatotionPipeline(object):
    '''
    This pipeline annotates items with a carwled_at date entry.
    '''
    def process_item(self, item, spider):  # @UnusedVariable
        item['crawled_at'] = datetime.now().strftime('%Y-%m-%d')
        return item


# end of file
