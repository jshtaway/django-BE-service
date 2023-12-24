import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def test_data():
    return {}


@pytest.fixture(scope="session")
def client():
    return APIClient()
