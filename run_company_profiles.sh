rm company_profiles.json
scrapy crawl campany_profiles -a input_file="./company_index.json" -o company_profiles.json -L INFO
python beautify_json.py company_profiles.json
echo
