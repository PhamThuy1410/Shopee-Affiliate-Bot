import re


def parse_shopee_url(url: str):
    """
    Parse Shopee URL to extract shop_id and item_id.

    Example:
    https://shopee.vn/product/88201679/23832839487
    """

    pattern = r"/product/(\d+)/(\d+)"

    match = re.search(pattern, url)

    if not match:
        return None

    return {
        "shop_id": match.group(1),
        "item_id": match.group(2)
    }