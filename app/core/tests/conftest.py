import pytest
from rest_framework.test import APIClient
from core.tests.pytest_patches import *


@pytest.fixture(scope="function")
def test_data():
    return {}


@pytest.fixture(scope="session")
def client():
    return APIClient()
