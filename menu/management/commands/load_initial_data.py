from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load initial data into PostgreSQL database'

    def handle(self, *args, **options):
        try:
            call_command('loaddata', 'fulldata.json')
            self.stdout.write(self.style.SUCCESS("✔ Data loaded successfully"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"✖ Error: {e}"))