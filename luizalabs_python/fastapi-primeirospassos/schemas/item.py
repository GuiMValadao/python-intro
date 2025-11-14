from pydantic import BaseModel


class ItemIn(BaseModel):
    item_id: int
    name: str | None = None
    existent: bool = False
