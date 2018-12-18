# -*- coding: utf-8 -*-

import re

from datetime import datetime
from scrapy.exceptions import DropItem


class ItemVerificationPipeline(object):
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
        for field, validator in fields:
            if not re.match(validator, item[field]):
                log_msg = "(DROPPED_ITEM_BAD_FIELD) Item dropped, invalid item field:\nitem:%s\nfield:%s\nvalue:%s"
                log_msg = log_msg % (repr(item), field, item[field])
                spider.logger.warn(log_msg)
                raise DropItem()
        return item


class CrawlTimeAnnotatotionPipeline(object):
    '''
    This pipeline annotates items with a carwled_at date entry.
    '''
    def process_item(self, item, spider):  # @UnusedVariable
        item['crawled_at'] = datetime.now().strftime('%Y-%m-%d')
        return item


# end of file
