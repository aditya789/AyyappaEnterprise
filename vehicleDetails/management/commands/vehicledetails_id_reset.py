# yourapp/management/commands/reset_ids.py

from django.core.management.base import BaseCommand
from vehicleDetails.models import VehicleDetail
from django.db import connections

class Command(BaseCommand):
    help = 'Reset ID column data for a specific model'

    def handle(self, *args, **options):
        # Get the model class
        model_class = VehicleDetail

        # Get the database connection
        connection = connections[model_class.objects.db]

        # Retrieve the table name for the model
        table_name = model_class._meta.db_table

        # Execute a raw SQL query to reset the ID sequence
        sql = f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), coalesce(max(id), 1), false) FROM {table_name};"
        with connection.cursor() as cursor:
            cursor.execute(sql)

        self.stdout.write(self.style.SUCCESS(f'Successfully reset ID column for {model_class.__name__}'))
