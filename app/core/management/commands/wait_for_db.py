"""
django will auto detect this file as a management command because of the folder infrastructure

This command will wait for the database to be available before continuing to run the other commands.
"""

from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    """built in command class and method to handle the command needs this structure"""
    help = 'Wait for database'

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except Exception as e:
                self.stdout.write('Database unavailable, waiting 1 second...')
                self.stdout.write(str(e))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
