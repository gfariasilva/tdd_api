from pydantic import Field

from store.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(..., description="Product's name")
    quantity: int = Field(..., description="Product's available quantity")
    price: float = Field(..., description="Product's price")
    status: bool = Field(..., description="Product's status")
