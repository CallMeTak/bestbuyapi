import json
import xml.etree.ElementTree as ET

import pytest
from pytest_httpx import HTTPXMock

from bestbuyapi.utils.exceptions import BestBuyAPIError


def test_validate_params(bbapi):
    with pytest.raises(BestBuyAPIError):
        payload = {"query": "some query", "params": {"fiz": "bazz", "wrong": None}}
        bbapi.category._validate_params(payload)


@pytest.mark.asyncio
async def test_json_response(bbapi, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        json={"products": [{"name": "Super Awesome Product"}]},
        headers={"Content-Type": "application/json; charset=UTF-8"},
    )
    query = "accessories.sku=5985609"
    response = await bbapi.products.search(query=query, format="json")
    assert isinstance(response, dict), "Response cannot be converted to JSON"


@pytest.mark.asyncio
async def test_xml_response(bbapi, httpx_mock: HTTPXMock):
    sku_nbr = 5985609
    httpx_mock.add_response(
        content=f"<products><product><sku>{sku_nbr}</sku></product></products>".encode(
            "utf-8"
        ),
        headers={"Content-Type": "application/xml; charset=UTF-8"},
    )

    query = f"sku={sku_nbr}"

    # leaving the format blank will default to xml
    response = await bbapi.products.search(query=query, format="xml")
    xml_tree = ET.fromstring(response)
    response_sku = xml_tree[0].findall("sku")[0].text
    assert int(response_sku) == sku_nbr, "XML Response parsing is failing"
