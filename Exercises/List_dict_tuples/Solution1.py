def store_order_records():
    """Task 1: Capture and store multiple orders"""
    orders = []
    n = int(input("Enter number of orders: "))
    for i in range(n):
        print(f"Order {i+1}")
        customer = input("Customer: ")
        product = input("Product: ")
        amount = float(input("Amount: "))
        orders.append((customer, product, amount))
        print()  # Blank line for readability
    return orders

def maintain_product_lookup():
    """Task 2: Store product details using dictionary"""
    product_lookup = {
        "Electronics": "Electronics - Gadgets & Devices",
        "Clothing": "Clothing - Apparel & Fashion",
        "Books": "Books - Literature & Education"
    }
    return product_lookup

def display_orders(orders, product_lookup):
    """Display all orders with product details"""
    print("\nAll Orders:")
    print("----------------------------------")
    for order in orders:
        prod_desc = product_lookup.get(order, order)
        print(f"Customer: {order} Product: {prod_desc} Amount: {order}")
    print("----------------------------------")

def filter_orders_by_product(orders, product_lookup):
    """Task 3: Display orders for a given product type"""
    search_product = input("Enter product type to filter: ")
    print(f"\nOrders in {product_lookup.get(search_product, search_product)}")
    print("----------------------------------")
    found = False
    for order in orders:
        if order[1].lower() == search_product.lower():  # Fixed: order[1] instead of order
            print(f"Customer: {order[0]} Amount: {order[2]}")
            found = True
    if not found:
        print("No orders found in this product type.")
    print("----------------------------------")


def main():
    """Task 4: Modularize logic using functions"""
    orders = store_order_records()  # Task 1
    product_lookup = maintain_product_lookup()  # Task 2
    display_orders(orders, product_lookup)
    filter_orders_by_product(orders, product_lookup)  # Task 3

main()  # Program Execution