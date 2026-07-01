from fastapi import APIRouter

from app.schemas.zalo import ZaloWebhook
from app.services.shopee_service import ShopeeService

router = APIRouter(prefix="/zalo", tags=["Zalo"])


@router.get("/webhook")
async def verify():
    return {
        "status": "ok"
    }


@router.post("/webhook")
async def webhook(data: ZaloWebhook):

    message = data.message.text

    result = ShopeeService.convert(message)

    print("=" * 60)
    print(result)
    print("=" * 60)

    return result