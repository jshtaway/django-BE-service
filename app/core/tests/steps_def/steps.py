from pytest_bdd import when, then, parsers

from psycopg2 import OperationalError as Psycopg2Error # error that may get thrown by db
from django.core.management import call_command
from django.db.utils import OperationalError # error that may get thrown by db
from django.test import SimpleTestCase


@when(parsers.parse('I wait for db ready'))
def wait_for_db_ready(patched_check_fixture):
    patched_check_fixture.return_value = True
    call_command('wait_for_db')
    patched_check_fixture.assert_called_once_with(database=['default'])


@then(parsers.parse('Django starts without error'))
def django_starts_without_ecception(test_data):
    pass
