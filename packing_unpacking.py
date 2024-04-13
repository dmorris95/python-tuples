#Task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Joe", "Laptop", 1),
    ("Steve", "TV", 2),
    ("Robert", "Headphones", 3)
]

def display_orders(order_data):
    for order_info in order_data:
        (name, product, quantity) = order_info
        print(f"Customer name: {name}\n\tProduct Ordered: {product} -- Quantity Ordered: {quantity}\n")

display_orders(orders)

