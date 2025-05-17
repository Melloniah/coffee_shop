import sys
sys.path.append('./')

from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

# ---------------------
# Create Sample Data
# ---------------------
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

# ---------------------
# Sample Interactions
# ---------------------

print("\n--- All Customers ---")
for customer in Customer.all():
    print(customer.name)

print("\n--- Coffees Ordered by Alice ---")
for coffee in alice.coffees():
    print(coffee.name)

print("\n--- Customers Who Ordered Espresso ---")
for customer in espresso.customers():
    print(customer.name)

print("\n--- Most Aficionado for Espresso ---")
print(espresso.most_aficionado().name)

# ---------------------
# Basic Validations
# ---------------------

def run_validations():
    print("\n--- Running Validation Tests ---")
    try:
        Order("not a customer", espresso, 4.00)
    except Exception:
        print("✔️  Rejected invalid customer")

    try:
        Order(alice, "not a coffee", 4.00)
    except Exception:
        print("✔️  Rejected invalid coffee")

    try:
        Order(alice, espresso, "free")
    except Exception:
        print("✔️  Rejected invalid price")

run_validations()
