from fastapi import APIRouter
from app.schemas.convert import ConvertRequest
from app.services.shopee import convert_link

router = APIRouter()


@router.post("/convert")
def convert(request: ConvertRequest):
    return convert_link(request.url)