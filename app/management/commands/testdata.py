from django.core.management.base import BaseCommand
from app.models import TestData1, TestData2, TestData3, TestData4, TestData5
import random

testdata = [TestData1, TestData2, TestData3, TestData4, TestData5]


class Command(BaseCommand):
    help = 'Populate the database with test data'

    def add_arguments(self,
                      parser):
        parser.add_argument('num_entries', type=int, help='Number of entries per model')

    def handle(self,
               *args,
               **options):
        num_entries = options['num_entries']

        nr = 1
        for x in testdata:
            for j in range(num_entries):
                name = f'Campaign {j}'
                cost = random.uniform(10, 100)
                revenue = random.uniform(20, 200)
                profit = revenue - cost
                roi = (profit / cost) * 100 if cost != 0 else 0

                x.objects.create(
                    name=name,
                    cost=cost,
                    revenue=revenue,
                    profit=profit,
                    roi=roi,
                )
            nr += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {num_entries} entries per model.'))
