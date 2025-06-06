
from lib.coffee import ALLOWED_SIZES
class Order:
    all=[]
    def __init__(self, customer, coffee, size, price):
        self.customer = customer    # Calls the setter
        self.coffee = coffee        # Calls the setter
        self.price = price          # Calls the setter
        Order.all.append(self)  # store every order created

    @property
    def customer(self):
        return self._customer

    @customer.setter #validates the customer class instance called here
    def customer(self, value):
        from lib.customer import Customer  # import here to avoid circular import
        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter #validates the Coffee class instance called here
    def coffee(self, value):
        from lib.coffee import Coffee  # import here to avoid circular import
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        self._coffee = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ALLOWED_SIZES:
            raise ValueError(f"size must be one of {ALLOWED_SIZES}")
        self._size = value

    @property #validates the price
    def price(self):
        return self._price

    @price.setter #validating the price
    def price(self, amount):
        if not isinstance(amount, float):
            raise TypeError("price must be a float")
        if not (1.0 <= amount <= 10.0):
            raise ValueError("Price must be between $1.00 and $10.00")
        self._price = amount


        