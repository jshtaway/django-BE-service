from core.tests.steps_def.steps import *
from pytest_bdd import scenario


@scenario('features/unit.feature', 'Test django management commands')
def test_db_wait():
    pass


@scenario('features/unit.feature', 'Test django DB delayed')
def test_db_delay():
    pass