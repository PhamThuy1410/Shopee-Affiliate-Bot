from fastapi import APIRouter

from app.schemas.convert import ConvertRequest
from app.schemas.response import ConvertResponse
from app.services.shopee_service import ShopeeService

router = APIRouter()


@router.post("/convert", response_model=ConvertResponse)
def convert(request: ConvertRequest):
    return ShopeeService.convert(request.url)