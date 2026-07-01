from typing import Optional
from pydantic import BaseModel


class Sender(BaseModel):
    id: str


class Message(BaseModel):
    text: str


class ZaloWebhook(BaseModel):
    event_name: str
    sender: Optional[Sender] = None
    message: Optional[Message] = None