import pytest

from bestbuyapi import BestBuyAPI


@pytest.fixture(scope="session")
def bbapi():
    """Returns a BestBuyAPI instance with a dummy API key."""
    yield BestBuyAPI("dummy_api_key")
