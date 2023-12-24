from app.tests.steps_def.steps import *
from pytest_bdd import scenario


@scenario('features/unit.feature', 'Add two numbers in add function')
def test_add_numbers():
    """test adding numbers"""
    pass


@scenario('features/views.feature', 'Greetings')
def test_add_numbers():
    """test adding numbers"""
    pass

