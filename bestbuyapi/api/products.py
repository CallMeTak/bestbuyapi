from typing import Any, Dict, Union
from ..api.base import BestBuyCore
from ..utils.exceptions import BestBuyProductAPIError
from ..constants import PRODUCT_DESCRIPTION_TYPES, PRODUCT_API


class BestBuyProductsAPI(BestBuyCore):
    def _api_name(self) -> str:
        return PRODUCT_API

    # =================================
    #   Search by description or SKU
    # =================================

    async def search_by_description(
        self, description_type: int, description: str, **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """Searches the product API using description parameter
        :params:
            :description_type (int): Integer from 1 to 4 to determine the type
                of description the call is going to use.
                The integers represent:
                    - 1: name
                    - 2: description
                    - 3: shortDescription
                    - 4: longDescription
            :description (str): description's content.
        """
        d_type = PRODUCT_DESCRIPTION_TYPES[description_type]
        payload = {"query": "{0}={1}".format(d_type, description), "params": kwargs}
        return await self._call(payload)

    async def search_by_sku(
        self, sku: Union[str, int], **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """Search the product API by SKU
        :params:
            :sky (str): SKU number of the desired product.
            :kwargs (dict): request parameters
        """
        payload = {"query": "sku={0}".format(sku), "params": kwargs}
        return await self._call(payload)

    async def search_by_review_criteria(
        self, review_type: int, review: float, **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """
        Searches the product API using the Review criteria.

        :param review_type: Integer, with customer review type the API
                            call will use.
                            The integer represent:
                            - 1: "customerReviewAverage"
                            - 2: "customerReviewCount"
        :param review: Float, with the actual value of the review to be
                       criteria to be search for.
                       - customerReviewAverage: should be a number  between
                         0.0 and 5.0
                       - customerReviewCount: should be a number  which is
                         greater than 0.

        """
        if review_type == 2:
            review = int(review)
        payload = {"query": "{0}={1}".format(review_type, review), "params": kwargs}
        return await self._call(payload)

    # =================================
    #         Custome Search
    # =================================

    async def search(
        self, query: str, **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """Performs a customized search on the BestBuy product API. Query
        parameters should be passed to function in a dictionary.

        :params:
            :query (str): String with query parameter. For examples of query
            check BestBuy documenation at https://goo.gl/jWboE2

        """
        payload = {"query": query, "params": kwargs}
        return await self._call(payload)
