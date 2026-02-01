# --------------------------------------
# Telco Customer Subscription Management System
# --------------------------------------

# ===== Task 1: Store Customer Records =====
# Capture and store multiple customers
def store_customer_records():
    customers = []
    n = int(input("Enter number of customers: "))

    for i in range(n):
        print(f"\nCustomer {i + 1}:")
        name = input("Name : ")
        city = input("City : ")
        plan = input("Plan : ")

        customers.append((name, city, plan))

    return customers


# ===== Task 2: Maintain Plan Lookup =====
# Store plan details using dictionary
def maintain_plan_lookup():
    plan_lookup = {
        "prepaid": "Prepaid Plan",
        "postpaid": "Postpaid Plan"
    }
    return plan_lookup


# ===== Task 3: Filter Customers by City =====
# Display customers for a given city
def filter_customers_by_city(customers, plan_lookup):
    search_city = input("\nEnter city to filter: ")

    print(f"\nCustomers in {search_city}:")
    print("----------------------------------")

    found = False

    for customer in customers:
        if customer[1].lower() == search_city.lower():
            print("Name :", customer[0])
            print("Plan :", customer[2])
            print()
            found = True

    if not found:
        print("No customers found in this city.")

    print("----------------------------------")


# ===== Task 4: Function Calls =====
# Modularize logic using functions
def main():
    customers = store_customer_records()            # Task 1
    plan_lookup = maintain_plan_lookup()             # Task 2
    filter_customers_by_city(customers, plan_lookup) # Task 3


# ===== Program Execution =====
main()
