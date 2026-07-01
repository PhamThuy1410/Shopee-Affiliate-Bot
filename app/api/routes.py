from fastapi import APIRouter

from app.schemas.convert import ConvertRequest
from app.schemas.response import ConvertResponse
from app.services.shopee_service import ShopeeService
from fastapi import HTTPException
from app.utils.exceptions import InvalidShopeeUrl

router = APIRouter()


@router.post("/convert", response_model=ConvertResponse)
def convert(request: ConvertRequest):

    try:
        return ShopeeService.convert(request.url)

    except InvalidShopeeUrl as e:

        raise HTTPException(
            status_code=400,
            detail=e.message
        )