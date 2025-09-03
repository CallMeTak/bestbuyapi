---
Python Best Buy API Wrapper
---

![image](https://img.shields.io/badge/version-3.0.0-blue.svg)

[![image](https://travis-ci.com/lv10/bestbuyapi.svg?branch=master)](https://travis-ci.com/lv10/bestbuyapi)

This is a small python wrapper implementation for BestBuy API. This
implementation does not cover all the APIs from BestBuy yet. As of now,
it only supports the calls to the Products, Categories, bulk and Cover
APIs. Locations and Reviews API are in the making.

The wrapper doesn\'t assume any design requirements on the user end.
Queries to the API endpoints are done similar to what you would put in
the browser with the convenience of having python prepare for you the
query, url, and interpret the response.

NOTICE: This project is only supported by python 3.7+.

# Features

- Query Bulk BestBuy API
- Query Stores BestBuy API (by id, currently)
- Query Products BestBuy API
- Query Categories BestBuy API
- Obtain queries result in JSON or XML

For details on how to use the Best Buy API go to:
<https://developer.bestbuy.com/documentation>

# Install

```{.sourceCode .bash}
$ pip install bestbuyapi
```

**How to use Product, Category, Store and Bulk APIs**

```{.sourceCode .python}
import asyncio
from bestbuyapi import BestBuyAPI

async def main():
    async with BestBuyAPI("YourSecretAPIKey") as bb:
        a_prod = await bb.products.search(query="sku=9776457", format="json")
        a_cat = await bb.category.search_by_id(category_id="abcat0011001", format="json")
        all_categories = await bb.bulk.archive("categories", "json")
        print(a_prod)
        print(a_cat)
        print(all_categories)

if __name__ == "__main__":
    asyncio.run(main())
```

# FAQ

- Is there any difference between /api.bestbuy.com/ and
  api.remix.bestbuy.com?

  A:// This is the response from BestBuy Dev department: \"There is no
  difference, they serve the same data - we just consolidated domains.
  The official url to use is api.bestbuy.com though.\"

Any questions please feel free to email me at: <luis@lv10.me>
