from django.core.management.base import BaseCommand
from django.db import connection

from ...models import MyModel


class Command(BaseCommand):

    def handle(self, *args, **options):
        list(MyModel.objects.filter(boolean_field=False))
        for q in connection.queries:
            print(q['sql'])
