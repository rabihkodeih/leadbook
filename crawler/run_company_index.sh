rm company_index.json
scrapy crawl campany_index -o company_index.json -L INFO
python beautify_json.py company_index.json
echo
