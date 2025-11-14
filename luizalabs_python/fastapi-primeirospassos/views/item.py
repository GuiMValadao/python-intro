from pydantic import BaseModel


class ItemOut(BaseModel):
    item_id: int
    name: str
