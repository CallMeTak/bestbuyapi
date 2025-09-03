import json
import pytest
from pytest_httpx import HTTPXMock

from bestbuyapi import BASE_URL, BestBuyAPI


@pytest.mark.asyncio
async def test_search_by_description(bbapi, httpx_mock: HTTPXMock):
    description_type = 1
    description = "iphone*"
    response_format = "json"
    httpx_mock.add_response(
        json={"products": [{"name": "iPhone"}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    response = await bbapi.products.search_by_description(
        description_type=description_type,
        description=description,
        format=response_format,
    )
    product_name = response["products"][0]["name"]
    assert "iphone" in product_name.lower(), "Description search failing"


@pytest.mark.asyncio
async def test_search_by_sku(bbapi, httpx_mock: HTTPXMock):
    sku_nbr = 5706617
    httpx_mock.add_response(
        json={"products": [{"sku": sku_nbr}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    response = await bbapi.products.search_by_sku(sku=sku_nbr, format="json")
    assert sku_nbr == response["products"][0]["sku"], "Product SKU by search fails"


@pytest.mark.asyncio
async def test_search(bbapi, httpx_mock: HTTPXMock):
    query = "sku in(5706617,6084400,2088495)"
    httpx_mock.add_response(
        json={"total": 3},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    result = await bbapi.products.search(query=query, format="json")
    assert result["total"] >= 2, "general search is failing to complete"


@pytest.mark.asyncio
async def test_search_by_review_criteria_average(bbapi, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        json={"products": [{"name": "Super Awesome Product"}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    response = await bbapi.products.search_by_review_criteria(
        review_type=1, review=4.5, format="json"
    )
    assert response["products"][0]["name"] == "Super Awesome Product"


@pytest.mark.asyncio
async def test_search_by_review_criteria_count(bbapi, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        json={"products": [{"name": "Super Awesome Product"}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    response = await bbapi.products.search_by_review_criteria(
        review_type=2, review=100, format="json"
    )
    assert response["products"][0]["name"] == "Super Awesome Product"
