**Coffee Shop App**
**Overview**
This Python project models a simple Coffee Shop system with three main classes:

Customer: Represents customers with validated names.

Coffee: Represents different coffees with validated name, size, price, and type.

Order: Links customers and coffees with an order price.

The system tracks all instances of each class and supports querying relationships between them, such as which coffees a customer ordered, who ordered a coffee, and which customer spent the most on a given coffee.

**Features**
**Customer**
Create customers with names validated to be between 1 and 15 characters.

Retrieve all orders placed by a customer.

Get a unique list of coffees ordered by the customer.

Create new orders associating the customer with a coffee and price.

Class method most_aficionado(coffee) returns the customer who spent the most money on a particular coffee.

**Coffee**
Create coffee instances with validated attributes:

name: minimum 3 characters.

size: must be "small", "medium", or "large".

price: between $1.00 and $10.00.

type_of_coffee: one of "latte", "espresso", "americano", "cappuccino", or "mocha".

Retrieve all orders containing this coffee.

Retrieve unique customers who ordered this coffee.

Count total orders and calculate average order price for the coffee.

**Order**
Represents an order linking a customer, coffee, and price.

All order instances are tracked globally.Design Details
Aggregation:
Customer and Coffee classes reference Order instances, which connect customers and coffees without ownership.

**Validation:**
Properties ensure valid data for names, coffee size, type, and price.

Instance tracking:
Each class has a class-level list all to store and access all instances.

**How to Run**
Make sure customer.py, coffee.py, and order.py are in the same directory or properly installed as modules.

Import and instantiate the classes as shown in the usage example.

Use methods on the classes to create and query orders and data.

**Future Improvements**
Add order date/time and filtering by date.

Support updating or canceling orders.

Integrate persistent storage (database or files).

Expand coffee attributes and customer profiles.

