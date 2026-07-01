from pydantic import BaseModel


class ConvertResponse(BaseModel):
    success: bool
    shop_id: str | None = None
    item_id: str | None = None
    message: str | None = None