# Leadbook Test Project

This is the test project for Leadbook. It has two parts:

1. Crawler
2. API

## Common Installation

Both parts are in one source control repository.
Before installation, make sure that `Python3.6`, `pip3` and `virtualenv` are all installed and working fine:

    apt-get update
    apt-get dist-upgrade
    apt-get install -y python3-dev virtualenv gcc libmysqlclient-dev

Clone the repository into a destination directory, cd into it then create your virtual env using

    virtualenv -p python3 env
    
and activate it by

    . env/bin/activate
    
Now you can install the requirements by

    pip3 install -r requirements.txt
        
This concludes the common installtion for the crawler and the api.


# 1. Crawler

The crawler was custom built using [**Scrapy**](https://scrapy.org). There are two spiders, one for crawling company index data (named "company_index") and the other for crawling company profiles data (named "company_profiles"). Before starting, make sure to cd into the crawler folder form the root repo folder.

## Crawling Company Index Data
To crawl company index, use:

    scrapy crawl company_index -o ../data/company_index.json -L INFO

The output will be saved under the path specified by the -o option which is "../data/company_index.json" in this case. As can be seen also the logging level is set to INFO. The resulting file will look something like this:

    [
      {
        "ticker_symbol": "AALI",
        "company_name": "Astra Agro Lestari Tbk",
        "url": "http://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/?kodeEmiten=AALI",
        "listing_date": "1997-12-09",
        "crawled_at": "2018-12-19"
      },
      {
        "ticker_symbol": "ABBA",
        "company_name": "Mahaka Media Tbk",
        "url": "http://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/?kodeEmiten=ABBA",
        "listing_date": "2002-04-03",
        "crawled_at": "2018-12-19"
      },
      ...
    ]

A convinient script can as well be used:

    bash run_company_index.sh
    
## Crawling Company Profiles Data
To crawl company index, use:

    scrapy crawl company_profiles -a input_file="../data/company_index.json" -o ../data/company_profiles.json -L INFO

The output will be saved under the path specified by the -o option which is "../data/company_profiles.json" in this case. As can be seen also the logging level is set to INFO. The input file is also supplied using -a option. The resulting file will look something like this:

    [
      {
        "company_name": "Astra Agro Lestari Tbk",
        "security_code": "AALI",
        "office_address": "Jl Pulo Ayang Raya Blok OR No. 1  Kawasan Industri Pulogadung  Jakarta",
        "email_address": "Investor@astra-agro.co.id",
        "country": "Indonesia",
        "phone": "461-65-55",
        "fax": "461-6655, 461-6677, 461-6688",
        "npwp": "01.334.427.0-054.000",
        "company_website": "http://www.astra-agro.co.id",
        "ipo_date": "1997-12-09",
        "board": "UTAMA",
        "sector": "AGRICULTURE",
        "sub_sector": "PLANTATION",
        "registrar": "PT. Raya Saham Registrar (dulu bernama PT. Risjad Salim Registra",
        "corporate_secretary": [
          {
            "name": "Mario Casimirus Surung Gultom",
            "email": "investor@astra-agro.co.id",
            "phone": "021-4616555"
          }
        ],
        "director": [
          {
            "name": "Santosa",
            "position": "PRESIDEN DIREKTUR"
          },
          ...
        ],
        "subsidiary": [
          {
            "name": "PT Agro Menararachmat",
            "type": "Perkebunan Sawit",
            "total_asset": 231178.0,
            "percentage": 99.99
          },
          ...
        ],
        "crawled_at": "2018-12-19"
      },
      {
        "company_name": "Mahaka Media Tbk",
        "security_code": "ABBA",
        "office_address": "Sahid Office Boutique, Blok G Jl Jend Sudirman Kav.86 Jakarta 10220",
        "email_address": "corsec@mahakamedia.com",
        "country": "Indonesia",
        "phone": "(021) 573 9203",
        "fax": "(021) 573 9210",
        "npwp": "01.609.052.4-017.000",
        "company_website": "www.mahakamedia.com",
        "ipo_date": "2002-04-03",
        "board": "PENGEMBANGAN",
        "sector": "TRADE, SERVICES & INVESTMENT",
        "sub_sector": "ADVERTISING, PRINTING AND MEDIA",
        "registrar": "PT. Adimitra Jasa Korpora",
        "corporate_secretary": [
          {
            "name": "S. Pramudityo Anggoro",
            "email": "corsec@mahakamedia.com",
            "phone": "021-5739203"
          }
        ],
        "director": [
          {
            "name": "Adrian Syarkawi",
            "position": "DIREKTUR UTAMA"
          },
          ...
        ],
        "subsidiary": [
          {
            "name": "PT REPUBLIKA MEDIA MANDIRI",
            "type": "PENERBITAN PERS",
            "total_asset": 136794322232.0,
            "percentage": 92.0
          },
          ...
        ],
        "crawled_at": "2018-12-19"
      },
      ...
    ]

A convinient script can as well be used:

    bash run_company_profiles.sh
    
## Logging and Verificiation

After any crawling operation, log files should be inspected for errors and warnings. If no log file is specified, logging will be directed to the standard output. To log to file use:

    scrapy crawl <spider_name> -a ... -o ... --logfile <logfile_path> -L <log_level>
    
`logfile_path` and `log_level` define the file path and minimum level of messages to log. There are five levels of logging listed in decreasing order:

    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG

For example if a level of `WARNING` is specified only log message of that level and above will be logged (`ERROR` and `CRITICAL`).

The two spiders (company_index) and (company_profiles) have a post logging verification pipelines attached to them. Every crawled item will be verified the pipelines according to a specified set of regex validators. In case of a validation error the following log warning message will be issued:

**WARNING: BAD_FIELD: invalid item field**

_Format_ :

    <log-date:yyyy-mm-dd> <log-time:hh:mm:ss> [<spider_name>] WARNING: BAD_FIELD: invalid item field:\n
    item:<item json object>\n
    field:<field have invalid value>
    value:<the invalid value>

_Example_ :
    
    2018-12-20 15:30:43 [company_profiles] WARNING: BAD_FIELD: invalid item field:
    item:{'company_name': 'Kedawung Setia Industrial Tbk', 'security_code': 'KDSI', 'office_address': 'Jl.Mastrip 862  Warugunung-Karangpilang  Surabaya', 'email_address': 'corsec@kdsi-ind.com', 'country': 'Indonesia', 'phone': '(031) 7661983', 'fax': '(031) 7661981', 'npwp': '01.132.928.1-054.000', 'company_website': 'NULL', 'ipo_date': '1996-07-29', 'board': 'PENGEMBANGAN', 'sector': 'CONSUMER GOODS INDUSTRY', 'sub_sector': 'HOUSEWARE', 'registrar': 'PT. Sinartama Gunita', 'corporate_secretary': [{'name': 'R. Koorniagung T. Purwo', 'email': 'koorniagung@kedawungsetia.com', 'phone': '031 7661971'}], 'director': [{'name': 'Ali Sugiharto Wibisono', 'position': 'PRESIDEN DIREKTUR'}, {'name': 'Permadi Al Suharto', 'position': 'DIREKTUR'}, {'name': 'R. Koorniagung Trikorandono Purwo', 'position': 'DIREKTUR'}], 'subsidiary': [{'name': 'PT Kedawung Setia Corrugated Carton Box Industrial', 'type': 'Industri kotak karton gelombang dan tempat penyimpanan telur', 'total_asset': 869527200355.0, 'percentage': 100.0}, {'name': 'PT Kedawung Setia Corrugated Carton Box Industrial', 'type': 'Industri kotak karton gelombang dan tempat penyimpanan telur', 'total_asset': 891156756543.0, 'percentage': 99.999}]}
    field:company_website
    value:NULL

On other conditions such as network errors or timeouts, standard scrapy log error messages will be produced.




# 2. API

text goes here
