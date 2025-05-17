from order import Order  # import order because its a different file

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
    def create_order(self, coffee, price):
        # This creates a new order, and it's automatically added to Order.all
        return Order(customer=self, price=price, coffee=coffee) #aggregation because they are referencing order and coffee. 


    @classmethod
    
    def most_aficionado(cls, coffee):
        # Dictionary to track total spent per customer for the given coffee
        spending = {}

        # Loop through all orders
        for order in Order.all:
            # Check if the order is for the coffee we want
            if order.coffee == coffee:
                # Get the customer
                cust = order.customer
                # Add order price to customer's total spending
                if cust in spending:
                    spending[cust] += order.price
                else:
                    spending[cust] = order.price

        # If no customers found for this coffee, return None
        if not spending:
            return None

        # Find the customer with the maximum total spending
        top_customer = max(spending, key=spending.get)
        return top_customer