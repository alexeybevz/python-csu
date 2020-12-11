import os
import pytest
from decimal import Decimal
from domain.product import Product
from domain.tshirt_product import TShirtProduct
from db_service import DbService
from whse_file_persistable import WhseFilePersistable

db = DbService()

def test_price_only_positive():
    product = Product()
    with pytest.raises(Exception) as e_info:
        result = product.price = -100

def test_qty_only_positive():
    product = Product()
    with pytest.raises(Exception) as e_info:
        result = product.qty = -100

def test_add_empty_product_deny():
    columns = { 'sku': '123', 'name': '123', 'qty': 1, 'manufacter': '12345', 'price': 100, 'size': 48, 'color': 'red' }
    product = TShirtProduct()
    result = 0

    for c in columns:
        try:
            db.add_product(product)
        except ValueError as err:
            result += 1
            setattr(product, c, columns[c])

    assert result == 7

def test_add_and_delete_product():
    p = TShirtProduct()
    p.sku = 'test_sku_1'
    p.name = 'test_name'
    p.qty = 1
    p.manufacter = 'manufacter1'
    p.price = 100
    p.size = 42
    p.color = 'black'
    db.add_product(p)
    db.delete_product(p.sku)
    assert db.is_product_exists(p.sku) == False

def test_report_by_manufacter():
    row1 = { 'sku': 'test_sku_1', 'name': '1', 'qty': 1, 'manufacter': 'mnf_1', 'price': 100, 'size': 48, 'color': 'red' }
    row2 = { 'sku': 'test_sku_2', 'name': '1', 'qty': 1, 'manufacter': 'mnf_1', 'price': 100, 'size': 48, 'color': 'red' }
    row3 = { 'sku': 'test_sku_3', 'name': '1', 'qty': 1, 'manufacter': 'mnf_2', 'price': 100, 'size': 48, 'color': 'red' }

    for row in [ row1, row2, row3]:
        p = TShirtProduct()
        for r in row:
            setattr(p, r, row[r])
        db.add_product(p)

    expected_keys = [ 'mnf_1', 'mnf_2' ]
    expected_values = [ 2, 1 ]

    actual = db.report_by_field('производитель')
    actual_keys = []
    actual_values = []
    for row in actual:
        f, count = row
        actual_keys.append(f)
        actual_values.append(count)

    print('Compare keys:')
    print(f'Expected: {expected_keys}')
    print(f'Actual  : {actual_keys}')
    print('Compare values:')
    print(f'Expected: {expected_values}')
    print(f'Actual  : {actual_values}')

    for row in [ row1, row2, row3]:
        db.delete_product(row['sku'])

    assert (expected_keys == actual_keys) and (expected_values == actual_values)

def test_report_by_size():
    row1 = { 'sku': 'test_sku_1', 'name': '1', 'qty': 1, 'manufacter': 'mnf_1', 'price': 100, 'size': 48, 'color': 'red' }
    row2 = { 'sku': 'test_sku_2', 'name': '1', 'qty': 1, 'manufacter': 'mnf_1', 'price': 100, 'size': 46, 'color': 'red' }
    row3 = { 'sku': 'test_sku_3', 'name': '1', 'qty': 1, 'manufacter': 'mnf_2', 'price': 100, 'size': 50, 'color': 'red' }
    row4 = { 'sku': 'test_sku_4', 'name': '1', 'qty': 1, 'manufacter': 'mnf_2', 'price': 100, 'size': 50, 'color': 'red' }
    row5 = { 'sku': 'test_sku_5', 'name': '1', 'qty': 1, 'manufacter': 'mnf_2', 'price': 100, 'size': 50, 'color': 'red' }

    for row in [ row1, row2, row3, row4, row5 ]:
        p = TShirtProduct()
        for r in row:
            setattr(p, r, row[r])
        db.add_product(p)

    expected_keys = [ Decimal('46.00'), Decimal('48.00'), Decimal('50.00') ]
    expected_values = [ 1, 1, 3 ]

    actual = db.report_by_field('размер')
    actual_keys = []
    actual_values = []
    for row in actual:
        f, count = row
        actual_keys.append(f)
        actual_values.append(count)

    print('Compare keys:')
    print(f'Expected: {expected_keys}')
    print(f'Actual  : {actual_keys}')
    print('Compare values:')
    print(f'Expected: {expected_values}')
    print(f'Actual  : {actual_values}')

    for row in [ row1, row2, row3, row4, row5 ]:
        db.delete_product(row['sku'])

    assert (expected_keys == actual_keys) and (expected_values == actual_values)

def test_parse_csv():
    parser = WhseFilePersistable(os.path.dirname(os.path.realpath(__file__)) + '/whse_test.csv')
    products = parser.get_data()
    assert (len(products) == 3)

def test_update_product():
    row = { 'sku': 'test_sku_1', 'name': '1', 'qty': 1, 'manufacter': 'mnf_1', 'price': 100, 'size': 48, 'color': 'red' }

    product = TShirtProduct()
    for r in row:
        setattr(product, r, row[r])

    db.add_product(product)

    product.name = 'new name'
    db.add_product(product)

    products = db.get_products()
    db_product = db.get_product(product.sku)
    db.delete_product(product.sku)

    assert ((len(products) == 1) and (db_product.name == 'new name'))