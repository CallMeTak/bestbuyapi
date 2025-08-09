from .constants import BASE_URL
from .api.stores import BestBuyStoresAPI
from .api.bulk import BestBuyBulkAPI
from .api.products import BestBuyProductsAPI
from .api.categories import BestBuyCategoryAPI


__version__ = "2.0.0"


import httpx


from types import TracebackType
from typing import Optional, Type


class BestBuyAPI:
    def __init__(self, api_key: str) -> None:
        """API's base class
        :params:
            :api_key (str): best buy developer API key.
        """
        self.api_key = api_key.strip()
        self.client = httpx.AsyncClient()
        self.bulk = BestBuyBulkAPI(self.api_key, self.client)
        self.products = BestBuyProductsAPI(self.api_key, self.client)
        self.category = BestBuyCategoryAPI(self.api_key, self.client)
        self.stores = BestBuyStoresAPI(self.api_key, self.client)

    async def __aenter__(self) -> "BestBuyAPI":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        await self.client.aclose()
