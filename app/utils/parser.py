import re


def parse_shopee_url(url: str):
    """
    Extract shop_id and item_id from Shopee URLs.

    Supported formats:

    https://shopee.vn/product/123/456

    https://shopee.vn/Ten-san-pham-i.123.456

    """

    patterns = [

        r"/product/(\d+)/(\d+)",

        r"-i\.(\d+)\.(\d+)"

    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:

            return {
                "shop_id": match.group(1),
                "item_id": match.group(2)
            }

    return None