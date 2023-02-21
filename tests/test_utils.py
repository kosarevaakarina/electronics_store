import pytest

from utils.utils import Electronic_store
import os

electronic_store = Electronic_store("Смартфон", 1000, 20)


def test_electronic_store_init():
    assert electronic_store.name == "Смартфон"
    assert electronic_store.price == 1000
    assert electronic_store.amount == 20
    assert electronic_store.discount == 0.85


def test_calculate_total_price():
    assert electronic_store.calculate_total_price() == 20000


def test_discount_price():
    assert electronic_store.discount_price() == 850


def test_name():
    electronic_store.name = 'Телефон'
    assert electronic_store.name == 'Телефон'
    with pytest.raises(Exception):
        electronic_store.name = "Длина наименования товара превышает 10 символов."


def test_instantiate_from_csv():
    Electronic_store.instantiate_from_csv(os.path.join("tests", "test.csv"))
    item = Electronic_store.all[-1]
    assert item.name == 'Мышка'
    assert item.price == '50'
    assert item.amount == '5'


def test_is_integer():
    assert Electronic_store.is_integer(5) is True
    assert Electronic_store.is_integer(5.0) is True
    assert Electronic_store.is_integer(5.5) is False
