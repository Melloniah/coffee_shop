from order import Order  # Make sure you import Order class if not in same file

class Customer:
    all = []  # Class variable to track all Customer instances

    def __init__(self, name):
        self.name = name  # Calls the setter for validation
        Customer.all.append(self)  # Add this customer to the global list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        """
        Return a list of all Order instances associated with this customer.
        """
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        """
        Return a unique list of Coffee instances this customer has ordered.
        """
        # Use a set to avoid duplicates
        unique_coffee_set = {order.coffee for order in self.orders()}
        return list(unique_coffee_set)
