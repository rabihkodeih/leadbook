import sys
import json

from django.core.management.base import BaseCommand
from api.models import Company, Secretary, Director, Subsidiary


class Command(BaseCommand):
    help = ('Imports data into the api database using an input json data file.\n'
            'Usage: python manage.py importdata <path_to_json_file>')

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path of the input json data file')

    def handle(self, *args, **options):

        # parse arguments
        data_source_path = options.get('json_file')

        # delete all existing models
        for model_class in [Subsidiary, Director, Secretary, Company]:
            model_class.objects.all().delete()

        # import data from input json file
        with open(data_source_path) as data_source:
            data = data_source.read()
            items = json.loads(data)
            for ith, item in enumerate(items):
                sys.stdout.write('Creating item %s of %s\n' % (ith + 1, len(items)))

                item.pop('crawled_at')
                secretaries = item.pop('corporate_secretary')
                directors = item.pop('director')
                subsidiaries = item.pop('subsidiary')

                company = Company.objects.create(**item)

                for secretary in secretaries:
                    secretary['company'] = company
                    Secretary.objects.create(**secretary)

                for director in directors:
                    director['company'] = company
                    Director.objects.create(**director)

                for subsidiary in subsidiaries:
                    subsidiary['company'] = company
                    Subsidiary.objects.create(**subsidiary)

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))


# end of file
