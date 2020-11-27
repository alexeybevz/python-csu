import pytest
from domain.product import Product

def test_price_only_positive():
    product = Product()
    with pytest.raises(Exception) as e_info:
        result = product.price = -100

def test_qty_only_positive():
    product = Product()
    with pytest.raises(Exception) as e_info:
        result = product.qty = -100