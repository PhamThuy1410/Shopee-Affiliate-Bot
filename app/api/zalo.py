from fastapi import APIRouter

from app.schemas.zalo import ZaloWebhook
from app.schemas.response import ConvertResponse
from app.services.shopee_service import ShopeeService
from app.utils.logger import logger
from fastapi import HTTPException
from app.utils.exceptions import InvalidShopeeUrl

router = APIRouter(prefix="/zalo", tags=["Zalo"])


@router.get("/webhook")
async def verify():
    return {
        "status": "ok"
    }


@router.post(
    "/webhook",
    response_model=ConvertResponse
)
async def webhook(data: ZaloWebhook):
    try:
        message = data.message.text
        result = ShopeeService.convert(message)
        logger.info(result)
        return result

    except InvalidShopeeUrl as e:
        raise HTTPException(
            status_code=400,
            detail=e.message
        )