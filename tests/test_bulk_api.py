import zipfile
from io import BytesIO
import pytest
from pytest_httpx import HTTPXMock

from bestbuyapi import BASE_URL, BestBuyAPI


def test_build_url(bbapi):
    sample_url = f"{BASE_URL}products.xml.zip"
    payload = {"query": "products.xml.zip", "params": {}}
    url, thePayload = bbapi.bulk._build_url(payload)
    assert sample_url == url, "URL construction has issues"
    assert thePayload.get("apiKey") is not None, "API Key is None"


@pytest.mark.asyncio
async def test_archive(bbapi, httpx_mock: HTTPXMock):
    archive_name = "categories"
    file_format = "xml"

    # Create a dummy zip file in memory
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("test.xml", "<test/>")
    zip_buffer.seek(0)

    httpx_mock.add_response(
        content=zip_buffer.read(), headers={"Content-Type": "application/zip"}
    )

    response = await bbapi.bulk.archive(archive_name, file_format)
    assert len(response) >= 1, "Response is empty"
    for _, data in response.items():
        assert isinstance(data, bytes), "XML data response is not bytes"


@pytest.mark.asyncio
async def test_archive_subset(bbapi, httpx_mock: HTTPXMock):
    """The only available subset is productsActive, all other subsets are empty.
    This tests makes sure that subsets are still supported.
    """
    subset_name = "productsSoftware"
    file_format = "json"

    # Create a dummy zip file in memory
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        zf.writestr("test.json", '{"test": "test"}')
    zip_buffer.seek(0)

    httpx_mock.add_response(
        content=zip_buffer.read(), headers={"Content-Type": "application/zip"}
    )

    response = await bbapi.bulk.archive_subset(subset_name, file_format)
    assert "test.json" in response
    assert response["test.json"] == {"test": "test"}


@pytest.mark.asyncio
async def test_archive_not_zip(bbapi, httpx_mock: HTTPXMock):
    archive_name = "categories"
    file_format = "xml"

    httpx_mock.add_response(
        content=b"not a zip file", headers={"Content-Type": "application/text"}
    )

    response = await bbapi.bulk.archive(archive_name, file_format)
    assert response == {}
