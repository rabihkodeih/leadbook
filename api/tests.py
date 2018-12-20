import os
import sys
import django
from unittest import TestCase
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.test')
django.setup()


class APITestCase(TestCase):

    def test_list_all_companies(self):
        sys.stdout.write('\ntest_list_all_companies')
        c = Client()
        resp = c.get('http://localhost:8000/companies', follow=True)
        data = resp.json()
        self.assertEqual(data.get('status_code'), 200)
        self.assertEqual(data.get('message'), 'successful')
        self.assertEqual(data.get('total_results'), 618)
        self.assertEqual(len(data.get('data')), 618)

    def test_filter_company_by_name(self):
        sys.stdout.write('\ntest_filter_company_by_name')
        c = Client()
        company_name = 'Asuransi Bina Dana Arta Tbk'
        resp = c.get('http://localhost:8000/companies/?company_name=%s' % company_name, follow=True)
        data = resp.json()
        self.assertEqual(data.get('status_code'), 200)
        self.assertEqual(data.get('message'), 'successful')
        self.assertEqual(data.get('total_results'), 1)
        self.assertEqual(len(data.get('data')), 1)
        self.assertEqual(data.get('data')[0].get('company_name'), company_name)

    def test_filter_company_by_ticker_symbol(self):
        sys.stdout.write('\ntest_filter_company_by_ticker_symbol')
        c = Client()
        ticker_symbol = 'AALI'
        resp = c.get('http://localhost:8000/company/%s/' % ticker_symbol, follow=True)
        data = resp.json()
        self.assertEqual(data.get('status_code'), 200)
        self.assertEqual(data.get('message'), 'successful')
        self.assertEqual(data.get('total_results'), 1)
        self.assertEqual(data.get('data').get('company_name'), 'Astra Agro Lestari Tbk')

    def test_company_pagination(self):
        sys.stdout.write('\ntest_company_pagination')
        c = Client()
        resp = c.get('http://localhost:8000/companies/?page=1&length=20', follow=True)
        data = resp.json()
        self.assertEqual(data.get('status_code'), 200)
        self.assertEqual(data.get('message'), 'successful')
        self.assertEqual(data.get('total_results'), 618)
        companies_whole = data.get('data')
        self.assertEqual(len(companies_whole), 20)

        resp = c.get('http://localhost:8000/companies/?page=1&length=10', follow=True)
        data = resp.json()
        self.assertEqual(data.get('status_code'), 200)
        self.assertEqual(data.get('message'), 'successful')
        self.assertEqual(data.get('total_results'), 618)
        companies_partial_a = data.get('data')
        self.assertEqual(len(companies_partial_a), 10)

        resp = c.get('http://localhost:8000/companies/?page=2&length=10', follow=True)
        data = resp.json()
        self.assertEqual(data.get('status_code'), 200)
        self.assertEqual(data.get('message'), 'successful')
        self.assertEqual(data.get('total_results'), 618)
        companies_partial_b = data.get('data')
        self.assertEqual(len(companies_partial_b), 10)

        self.assertEqual(companies_whole, companies_partial_a + companies_partial_b)


# end of file
