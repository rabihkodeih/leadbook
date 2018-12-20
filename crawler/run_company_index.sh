rm ../data/company_index.json
scrapy crawl company_index -o ../data/company_index.json -L INFO
python beautify_json.py ../data/company_index.json
echo
