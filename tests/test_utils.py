from utils.utils import Electronic_store

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

