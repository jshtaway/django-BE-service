from pytest_bdd import when, then, parsers
from app.calc import add


@when(parsers.parse('I add "{x}" and "{y}"'))
def use_add(test_data, x, y):
    test_data["add"] = add(int(x), int(y))


@then(parsers.parse('the result should be "{z}"'))
def assert_addition(test_data, z):
    assert int(z) == test_data['add']


@when(parsers.parse('I go to "{uri}"'))
def client_get(test_data, client, uri):
    test_data['get'] = client.get(uri)


@then(parsers.parse('I get {response} in response'))
def step_function(test_data, response):
    assert test_data['get'] == response
