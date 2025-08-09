import json
import pytest
from pytest_httpx import HTTPXMock

from bestbuyapi import BASE_URL, BestBuyAPI


api_name = "categories"


def test_build_url(bbapi):

    sample_url = f"{BASE_URL}{api_name}(sku=43900)"
    payload = {"query": "sku=43900", "params": {"format": "json"}}
    url, thePayload = bbapi.category._build_url(payload)
    assert sample_url == url, "Sample url is different built url"
    assert thePayload["format"] == "json", "Response format isn't JSON"
    assert thePayload.get("apiKey") is not None, "Response doesn't have API Key"


@pytest.mark.asyncio
async def test_search_category_by_id(bbapi, httpx_mock: HTTPXMock):
    cat_id = "cat00000"
    httpx_mock.add_response(
        json={"categories": [{"id": cat_id}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    query = f"id={cat_id}"
    resp = await bbapi.category.search(query=query, show="id", format="json")
    assert resp["categories"][0]["id"] == cat_id, "Returned category id is different"


@pytest.mark.asyncio
async def test_search_category_by_name(bbapi, httpx_mock: HTTPXMock):
    cat_name = "Sony"
    httpx_mock.add_response(
        json={"categories": [{"name": cat_name}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    query = f"name={cat_name}"
    resp = await bbapi.category.search(query=query, format="json")
    assert (
        resp["categories"][0]["name"] == cat_name
    ), "Response category name is different"


@pytest.mark.asyncio
async def test_search_by_id(bbapi, httpx_mock: HTTPXMock):
    cat_id = "cat00000"
    httpx_mock.add_response(
        json={"categories": [{"id": cat_id}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    resp = await bbapi.category.search_by_id(category_id=cat_id, format="json")
    assert resp["categories"][0]["id"] == cat_id, "Returned category id is different"


@pytest.mark.asyncio
async def test_search_by_name_direct(bbapi, httpx_mock: HTTPXMock):
    cat_name = "Sony"
    httpx_mock.add_response(
        json={"categories": [{"name": cat_name}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    resp = await bbapi.category.search_by_name(category=cat_name, format="json")
    assert (
        resp["categories"][0]["name"] == cat_name
    ), "Response category name is different"
