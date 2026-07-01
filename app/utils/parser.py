import re
import httpx

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

def expand_short_url(url: str) -> str:
    """
    Mở rộng link rút gọn Shopee.
    Nếu không phải link rút gọn thì trả lại URL ban đầu.
    """

    if "s.shopee.vn" not in url:
        return url

    response = httpx.get(
        url,
        follow_redirects=True,
        timeout=10
    )
    return str(response.url)