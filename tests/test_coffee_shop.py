import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

@pytest.fixture
def setup_data():
    # Reset class variables before each test to avoid test pollution
    Customer._all = []
    Coffee._all = []
    Order._all = []

    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")

    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    Order(alice, latte, 5.00)
    Order(bob, espresso, 4.50)
    Order(alice, espresso, 4.00)
    Order(charlie, espresso, 3.50)
    Order(charlie, latte, 5.00)

    return {
        "alice": alice,
        "bob": bob,
        "charlie": charlie,
        "latte": latte,
        "espresso": espresso
    }

def test_customer_orders(setup_data):
    alice = setup_data["alice"]
    assert len(alice.orders()) == 2

def test_coffee_customers(setup_data):
    espresso = setup_data["espresso"]
    customer_names = {c.name for c in espresso.customers()}
    assert customer_names == {"Alice", "Bob", "Charlie"}

def test_most_aficionado(setup_data):
    espresso = setup_data["espresso"]
    aficionado = espresso.most_aficionado()
    assert aficionado.name in {"Alice", "Charlie"}  # Depending on your logic

def test_invalid_customer_raises():
    with pytest.raises(Exception):
        Order("not a customer", Coffee("Fake"), 4.00)

def test_invalid_coffee_raises():
    with pytest.raises(Exception):
        Order(Customer("Test"), "not a coffee", 4.00)

def test_invalid_price_raises():
    with pytest.raises(Exception):
        Order(Customer("Test"), Coffee("Fake"), "free")
