from fastapi import APIRouter

from app.schemas.convert import ConvertRequest
from app.services.shopee_service import ShopeeService

router = APIRouter()


@router.post("/convert")
def convert(request: ConvertRequest):

    return ShopeeService.convert(request.url)