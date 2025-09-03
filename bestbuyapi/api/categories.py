from typing import Any, Dict, Union
from ..api.base import BestBuyCore
from ..constants import CATEGORY_API
from ..utils.exceptions import BestBuyCategoryAPIError


class BestBuyCategoryAPI(BestBuyCore):
    def _api_name(self) -> str:
        return CATEGORY_API

    # =================================
    #   Search by description or SKU
    # =================================

    async def search(self, query: str, **kwargs: Any) -> Union[Dict[str, Any], bytes]:
        """
        Performs a customized search on the BestBuy category API. Query
        parameters should be passed to function in as a string.

        :param query: String with query parameter. For examples of query
                      check BestBuy documenation at https://goo.gl/ZH5mnP
        """
        payload = {"query": query, "params": kwargs}
        return await self._call(payload)

    async def search_by_id(
        self, category_id: str, **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """
        Search the category API by id

        :param id: string, with the id of the desired category.
        :param kwargs: dictionary, with request parameters
        """

        payload = {"query": f"id={category_id}", "params": kwargs}

        return await self._call(payload)

    async def search_by_name(
        self, category: str, **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """Search the category API by name
        :params:
            :name (str): string, with the name of the desired category.
            :kwargs (dict): dictionary, with request parameters
        """
        payload = {"query": "name={0}".format(category), "params": kwargs}
        return await self._call(payload)
