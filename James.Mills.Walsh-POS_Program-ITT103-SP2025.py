# ====== PY WIZARDS POS SYSTEM IMPLEMENTATION ======

# Predefined product catalog (dictionary)
products = {
    "Bread": {"price": 1150, "stock": 10},
    "Milk": {"price": 2500, "stock": 15},
    "Eggs": {"price": 500, "stock": 12},
    "Butter": {"price": 400, "stock": 8},
    "Juice": {"price": 650, "stock": 20},
    "Rice": {"price": 350, "stock": 25},
    "Sugar": {"price": 200, "stock": 18},
    "Flour": {"price": 380, "stock": 20},
    "Cooking Oil": {"price": 700, "stock": 10},
    "Cereal": {"price": 450, "stock": 61}
}

# Shopping cart (list of dictionaries)
cart = []

# Display product catalog
def display_products():
    print("\n--- Product Catalog ---")
    for name, details in products.items():
        print(f"{name}: ${details['price']} - Stock: {details['stock']}")

# Add item to cart
def add_to_cart():
    display_products()
    product_name = input("Enter the product name to add to cart: ").title()
    if product_name in products:
        if products[product_name]['stock'] > 0:
            try:
                quantity = int(input("Enter quantity: "))
                if 0 < quantity <= products[product_name]['stock']:
                    cart.append({"name": product_name, "price": products[product_name]['price'], "quantity": quantity})
                    products[product_name]['stock'] -= quantity
                    print(f"Added {quantity} x {product_name} to cart.")
                else:
                    print("Invalid quantity or insufficient stock.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Product out of stock.")
    else:
        print("Product not found.")

# View cart
def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        total = 0
        print("\n--- Shopping Cart ---")
        for item in cart:
            item_total = item['price'] * item['quantity']
            print(f"{item['name']} - {item['quantity']} pcs x ${item['price']} = ${item_total}")
            total += item_total
        print(f"Subtotal: ${total}")

# Remove item from cart
def remove_from_cart():
    if not cart:
        print("Your cart is empty.")
        return
    view_cart()
    product_name = input("Enter the product name to remove: ").title()
    found = False
    for item in cart:
        if item['name'] == product_name:
            products[product_name]['stock'] += item['quantity']
            cart.remove(item)
            print(f"Removed {product_name} from cart.")
            found = True
            break
    if not found:
        print("Product not found in cart.")

# Checkout and payment
def checkout():
    if not cart:
        print("Your cart is empty.")
        return
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    discount = 0.05 * subtotal if subtotal > 5000 else 0
    taxable_subtotal = subtotal - discount
    tax = 0.10 * taxable_subtotal
    total_due = taxable_subtotal + tax

    print(f"\nSubtotal: ${subtotal}")
    if discount:
        print(f"Discount (5%): -${discount:.2f}")
    print(f"Sales Tax (10%): ${tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")

    while True:
        try:
            amount_paid = float(input("Enter amount received: $"))
            if amount_paid >= total_due:
                change = amount_paid - total_due
                print_receipt(subtotal, discount, tax, total_due, amount_paid, change)
                cart.clear()
                break
            else:
                print("Amount paid is less than the total due.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

# Receipt generation
def print_receipt(subtotal, discount, tax, total_due, amount_paid, change):
    print("\n=========== Supreme Food Supermarket ===========")
    print("========= CUSTOMER RECEIPT =========")
    for item in cart:
        item_total = item['price'] * item['quantity']
        print(f"{item['name']} | {item['quantity']} pcs | ${item['price']} each | Total: ${item_total}")
    print("-------------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount:
        print(f"Discount: -${discount:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    print(f"Change: ${change:.2f}")
    print("Thank you for shopping with us!")
    print("=====================================")

# Low-stock alert
def check_low_stock():
    for name, details in products.items():
        if details['stock'] < 5:
            print(f"[LOW STOCK] {name} - Only {details['stock']} left!")

# Main program loop
while True:
    print("\n====== POS MAIN MENU ======")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Select an option (1-6): ")

    if choice == "1":
        display_products()
        check_low_stock()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        remove_from_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("Exiting POS System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 6.")