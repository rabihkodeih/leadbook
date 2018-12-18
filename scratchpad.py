'''
Created on Dec 18, 2018

@author: rabihkodeih
'''

import re

if __name__ == '__main__':
    print("Strating\n")

    item = {
        "ticker_symbol": "AALI",
        "company_name": "Astra Agro Lestari Tbk",
        "url": "http://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/?kodeEmiten=AALI",
        "listing_date": "1997-12-09",
        "crawled_at": "2018-12-18"
    }

    if not re.match('^[A-Z][A-Z][A-Z][A-Z]$', item['ticker_symbol']):
        print('not good')
    else:
        print('good')

    if not re.match('^.+$', item['company_name']):
        print('not good')
    else:
        print('good')

    if not re.match('^\d\d\d\d-\d\d-\d\d$', item['listing_date']):
        print('not good')
    else:
        print('good')

    print("\nDone")

    print(repr(item))


# end of file
