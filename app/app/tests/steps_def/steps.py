from pytest_bdd import given, when, then, parsers
from app.calc import add


@when(parsers.parse('I add "{x}" and "{y}"'))
def use_add(test_data, x, y):
    test_data["add"] = add(int(x), int(y))

@then(parsers.parse('the result should be "{z}"'))
def assert_addition(test_data, z):
    assert int(z) == test_data['add']
