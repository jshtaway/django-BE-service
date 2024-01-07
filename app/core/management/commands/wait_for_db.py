"""
Django command to wait for the database to be available
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError
 # error that may get thrown by db
from django.db.utils import OperationalError # error that may get thrown by db

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write('\n\nWaiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
