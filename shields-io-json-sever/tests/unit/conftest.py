import pytest
from API import app

@pytest.fixture
def client():
    """Creates the test client"""

    test_client = app.test_client()
    return test_client