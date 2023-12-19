from pytest_bdd import given, when, then, parsers
from app.calc import add


@when(parsers.parse('I add {x} and {y}'))
def add(test_data, x, y):
    test_data["add"] = add(x, y)

@then(parsers.parse('the result should be {z}'))
def assert_addition(test_data, z):
    assert z == test_data['add']
