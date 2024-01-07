import logging
import pytest
from rest_framework.test import APIClient
from unittest.mock import patch

@pytest.fixture(scope="function")
def test_data():
    return {}


@pytest.fixture(scope="session")
def client():
    return APIClient()

# -- MOCK --
@pytest.fixture(scope="function")
def patched_check(capsys):
    with patch('core.management.commands.wait_for_db.Command.check') as p:
        yield p
    # Capture the output
    captured = capsys.readouterr()
    logging.info(captured.out)
    
    logging.info("patched_check finished")


@pytest.fixture(scope="function")
def time_sleep(capsys):
    with patch('time.sleep') as p:
        yield p
    captured = capsys.readouterr()
    logging.info(captured.out)
    logging.info("patched_check finished")