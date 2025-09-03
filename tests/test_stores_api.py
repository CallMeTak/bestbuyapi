import json
import pytest
from pytest_httpx import HTTPXMock

from bestbuyapi import BestBuyAPI


@pytest.mark.asyncio
async def test_search(bbapi, httpx_mock: HTTPXMock):
    store_id = 281
    response_format = "json"
    httpx_mock.add_response(
        json={"stores": [{"storeId": store_id}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    response = await bbapi.stores.search_by_id(
        store_id=store_id, format=response_format
    )
    assert store_id == response["stores"][0]["storeId"], "Store by id not found"
