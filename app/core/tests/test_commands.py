from pytest_bdd import when, then, parsers
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OpError # error that may get thrown by db
from django.core.management import call_command
from django.db.utils import OperationalError # error that may get thrown by db
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    """test commands"""

    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(database=['default'])
