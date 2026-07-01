from app.utils.parser import parse_shopee_url


def convert_link(url: str):

    result = parse_shopee_url(url)

    if result is None:
        return {
            "success": False,
            "message": "Invalid Shopee URL"
        }

    return {
        "success": True,
        "shop_id": result["shop_id"],
        "item_id": result["item_id"]
    }