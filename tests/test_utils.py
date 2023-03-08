import pytest

from utils.utils import ElectronicStore, Phone, ClassMix, KeyBoard
import os


@pytest.fixture
def electronic_store():
    return ElectronicStore("Смартфон", 1000, 20)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def key_board():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_electronic_store_init(electronic_store):
    assert electronic_store.name == "Смартфон"
    assert electronic_store.price == 1000
    assert electronic_store.amount == 20
    assert electronic_store.discount == 0.85


def test_calculate_total_price(electronic_store):
    assert electronic_store.calculate_total_price() == 20000


def test_discount_price(electronic_store):
    assert electronic_store.discount_price() == 850


def test_name(electronic_store):
    electronic_store.name = 'Телефон'
    assert electronic_store.name == 'Телефон'
    with pytest.raises(Exception):
        electronic_store.name = "ДлинноеНазвание"


def test_instantiate_from_csv(electronic_store):
    ElectronicStore.instantiate_from_csv(os.path.join("tests", "test.csv"))
    item = ElectronicStore.all[-1]
    assert item.name == 'Мышка'
    assert item.price == '50'
    assert item.amount == '5'


def test_is_integer(electronic_store):
    assert ElectronicStore.is_integer(5) is True
    assert ElectronicStore.is_integer(5.0) is True
    assert ElectronicStore.is_integer(5.5) is False


def test_repr(electronic_store):
    assert electronic_store.__repr__() == 'ElectronicStore(Смартфон, 1000, 20)'


def test_str(electronic_store):
    assert electronic_store.__str__() == 'Смартфон'


def test_add(electronic_store):
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone + electronic_store == 25


def test_phone_init(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.amount == 5
    assert phone.number_of_sim == 2


def test_phone_number_of_sim(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_phone_repr(phone):
    assert repr(phone) == 'Phone(iPhone 14, 120000, 5, 2)'


def test_class_mix_init(key_board):
    assert key_board.name == 'Dark Project KD87A'
    assert key_board.price == 9600
    assert key_board.amount == 5


def test_class_mix_language(key_board):
    assert key_board.language == 'EN'


def test_class_mix_change_lang(key_board):
    key_board.change_lang()
    assert key_board.language == 'RU'
