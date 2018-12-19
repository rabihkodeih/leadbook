rm ../data/company_profiles.json
scrapy crawl campany_profiles -a input_file="../data/company_index.json" -o ../data/company_profiles.json -L INFO
python beautify_json.py ../data/company_profiles.json
echo
