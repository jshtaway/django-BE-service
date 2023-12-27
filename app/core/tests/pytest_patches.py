import pytest
from unittest.mock import patch

# mocks from unittest.mock built in libraries

@pytest.fixture(scope="function", autouse=False)
@patch('core.management.commands.wait_for_db.Command.check')
def patched_check(patched_check):
    # Start and stop the patch around the scenario
    return patched_check


@pytest.fixture(scope="function", autouse=False)
@patch('time.sleep')
def patched_sleep(patched_sleep):
    # Start and stop the patch around the scenario
    return patched_sleep
