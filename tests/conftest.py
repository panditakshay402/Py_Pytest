import pytest

@pytest.fixture
def valid_transfer_data():
    return {
        "from_account": "ACC-001",
        "to_account": "ACC-002",
        "amount": 250.00
    }