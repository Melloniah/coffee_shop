from order import Order  # Import Order class to establish relationships

class Coffee:
    all = []  # Class variable to store all instances of Coffee

    def __init__(self, name, size, price, type_of_coffee):
        # Initialize the coffee attributes
        self.name = name               # Calls the name setter for validation
        self.size = size               # Size of the coffee (validated)
        self.price = price             # Price of the coffee (validated)
        self.type_of_coffee = type_of_coffee  # Type, e.g., Latte, Espresso, etc.
        Coffee.all.append(self)        # Add this coffee instance to the class list

    @property
    def name(self):
        # Getter method for the coffee's name
        return self._name

    @name.setter
    def name(self, value):
        # Setter with validation: name must be at least 3 characters
        if len(value) < 3:
            raise ValueError("Name must be at least three characters long")
        self._name = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        allowed_sizes = ["small", "medium", "large"]
        if value not in allowed_sizes:
            raise ValueError(f"Size must be one of {allowed_sizes}")
        self._size = value

    @property
    def type_of_coffee(self):
        return self._type_of_coffee

    @type_of_coffee.setter
    def type_of_coffee(self, value):
        allowed_types = ["latte", "espresso", "americano", "cappuccino", "mocha"]
        if not isinstance(value, str):
            raise TypeError("type_of_coffee must be a string")
        if value.lower() not in allowed_types:
            raise ValueError(f"type_of_coffee must be one of: {', '.join(allowed_types)}")
        self._type_of_coffee = value.lower()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("price must be a number")
        if not (1.0 <= float(value) <= 10.0):
            raise ValueError("Price must be between $1.00 and $10.00")
        self._price = float(value)

    def orders(self):
        """Return all orders associated with this Coffee instance."""
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        """
        Return a unique list of customers who have ordered this coffee.
        """
        unique_customers = {order.customer for order in self.orders()}
        return list(unique_customers)

    def num_orders(self):
        """Count how many times this coffee has been ordered."""
        return len([order for order in Order.all if order.coffee == self])

    def average_price(self):
        """Calculate the average price of this coffee across orders."""
        coffee_orders = [order for order in Order.all if order.coffee == self]
        if coffee_orders:
            total_price = sum(order.price for order in coffee_orders)
            return total_price / len(coffee_orders)
        return 0
