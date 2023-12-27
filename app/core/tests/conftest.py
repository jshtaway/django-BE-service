import pytest
from rest_framework.test import APIClient
from unittest.mock import patch

# Apply the patch at the module level
patched_check = patch('core.management.commands.wait_for_db.Command.check')

@pytest.fixture(scope="function", autouse=False)
def patched_check_fixture():
    # Start and stop the patch around the scenario
    patched_check.start()
    yield patched_check
    patched_check.stop()


@pytest.fixture(scope="function")
def test_data():
    return {}


@pytest.fixture(scope="session")
def client():
    return APIClient()
