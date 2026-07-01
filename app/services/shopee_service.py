from app.utils.parser import parse_shopee_url, expand_short_url
from app.utils.logger import logger

class ShopeeService:

    @staticmethod
    def convert(url: str):

        logger.info(f"Receive URL: {url}")
        url = expand_short_url(url)
        logger.info(f"Expanded URL: {url}")
        result = parse_shopee_url(url)

        if result is None:
            logger.error("Invalid Shopee URL")
            return {
                "success": False,
                "message": "Invalid Shopee URL"
            }

        logger.success(result)
        return {
            "success": True,
            "shop_id": result["shop_id"],
            "item_id": result["item_id"]
        }