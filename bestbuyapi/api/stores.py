from typing import Any, Dict, Union
from ..api.base import BestBuyCore
from ..constants import STORES_API
from ..utils.exceptions import BestBuyStoresAPIError


class BestBuyStoresAPI(BestBuyCore):
    def _api_name(self) -> str:
        return STORES_API

    # =================================
    #   Search by store by name or id
    # =================================

    async def search_by_id(
        self, store_id: Union[str, int], **kwargs: Any
    ) -> Union[Dict[str, Any], bytes]:
        """Searches the stores api given an id"""
        payload = {"query": f"storeId={store_id}", "params": kwargs}
        return await self._call(payload)
