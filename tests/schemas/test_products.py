import pytest
from pydantic import ValidationError

from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    product = ProductIn(**product_data())

    assert product.name == "Iphone 14 Pro Max"


def test_schemas_return_raise():
    data = {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.500}

    with pytest.raises(ValidationError) as error:
        ProductIn(**data)

    assert error.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.11/v/missing",
    }
