from order import Order  # Import Order class to establish relationships

class Coffee:
    all = []  # Class variable to store all instances of Coffee

    def __init__(self, name, size, price, type_of_coffee):
        # Initialize the coffee attributes
        self.name = name               # Calls the name setter for validation
        self.size = size               # Size of the coffee (not yet validated)
        self.price = price             # Price of the coffee (not yet validated)
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

    def orders(self):
        """
        Return all orders associated with this Coffee instance.
        Filters through all Order instances and picks only those where the
        order.coffee matches this coffee.
        """
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        """
        Return a unique list of customers who have ordered this coffee.
        - First, get all orders of this coffee using self.orders()
        - Then, collect the customer from each order
        - Use a set to ensure uniqueness
        - Convert the set back to a list before returning
        """
        unique_customers = {order.customer for order in self.orders()}
        return list(unique_customers) #self.orders is the method above being called. 
