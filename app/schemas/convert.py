from pydantic import BaseModel


class ConvertRequest(BaseModel):
    url: str