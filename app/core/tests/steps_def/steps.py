from pytest_bdd import when, then, parsers
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error # error that may get thrown by db
from django.core.management import call_command
from django.db.utils import OperationalError # error that may get thrown by db
from django.test import SimpleTestCase


@when(parsers.parse('I wait for db ready'))
def wait(patched_check):
    patched_check.return_value = True
    call_command('wait_for_db')


@when(parsers.parse('I wait for db delay'))
def wait(patched_check, patched_sleep):
    patched_check.side_effect = (
        [Psycopg2Error] * 2 + # hasnt started yet
        [OperationalError] * 3 + # hasnt setup test db yet
        [True]
    )
    call_command('wait_for_db')
    assert (
        patched_check.call_count == 6,
        f"{patched_check.call_count} != 6"
    )
    patched_check.assert_called_with(databases=['default'])


@then(parsers.parse('Django starts without error'))
def django_starts_without_ecception(patched_check):
    patched_check.assert_called_once_with(databases=['default'])


@then(parsers.parse('Test errors'))
def django_starts_without_ecception(patched_check):
    pass