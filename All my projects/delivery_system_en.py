"""
Restaurant Delivery Ordering System
"""

# ===== RESTAURANT DATABASE =====

# Restaurant menu organized by category
menu = {
    "appetizers": {
        "Nachos": {"price": 8.50, "time": 10, "points": 50},
        "BBQ Wings": {"price": 12.00, "time": 15, "points": 80},
        "Caesar Salad": {"price": 9.00, "time": 8, "points": 60},
        "Croquettes": {"price": 7.50, "time": 12, "points": 45}
    },
    "main_courses": {
        "Margherita Pizza": {"price": 15.00, "time": 20, "points": 100},
        "Pepperoni Pizza": {"price": 16.50, "time": 20, "points": 110},
        "Classic Burger": {"price": 13.50, "time": 18, "points": 90},
        "BBQ Burger": {"price": 14.50, "time": 18, "points": 95},
        "Carbonara Pasta": {"price": 14.00, "time": 15, "points": 95},
        "Bolognese Pasta": {"price": 13.00, "time": 15, "points": 85}
    },
    "desserts": {
        "Ice Cream": {"price": 5.00, "time": 2, "points": 30},
        "Cheesecake": {"price": 6.50, "time": 3, "points": 40},
        "Brownie": {"price": 5.50, "time": 3, "points": 35},
        "Flan": {"price": 4.50, "time": 2, "points": 25}
    },
    "drinks": {
        "Soda": {"price": 3.00, "time": 1, "points": 15},
        "Water": {"price": 2.00, "time": 1, "points": 10},
        "Fresh Juice": {"price": 4.50, "time": 3, "points": 25},
        "Coffee": {"price": 2.50, "time": 2, "points": 15}
    }
}

# VIP customer database with accumulated points
vip_customers = {
    "juan": {"points": 500, "orders": 12},
    "maria": {"points": 1200, "orders": 28},
    "pedro": {"points": 300, "orders": 7},
    "ana": {"points": 850, "orders": 19},
    "luis": {"points": 150, "orders": 3}
}

# Special combos of the day (sets for the items)
daily_combos = {
    "Italian Combo": {
        "items": {"Margherita Pizza", "Soda"},
        "discount": 15  # Discount percentage
    },
    "Burger Combo": {
        "items": {"Classic Burger", "Nachos", "Soda"},
        "discount": 20
    },
    "Light Combo": {
        "items": {"Caesar Salad", "Water", "Flan"},
        "discount": 10
    }
}

# ===== SYSTEM FUNCTIONS =====

def show_welcome():
    """Displays the restaurant's welcome message."""
    print("=" * 60)
    print(" " * 15 + "🍕 Welcome to Python Eats! 🍕")
    print("=" * 60)
    print()


def verify_customer():
    """
    Checks whether the customer is registered and returns their information.

    Returns:
        tuple: (customer_name, available_points, is_vip)
    """
    is_customer = ""
    while is_customer not in ["y", "n", "yes", "no"]:
        is_customer = input("Are you a registered customer? (y/n): ")
        if is_customer not in ["y", "n", "yes", "no"]:
            print("❌ Please enter 'y' for yes or 'n' for no.")

    if is_customer in ["y", "yes"]:
        name = input("Enter your name: ")

        if name in vip_customers:
            points = vip_customers[name]["points"]
            print(f"\n✨ Hi {name}! You have {points} accumulated points.")
            print(f"📊 You've placed {vip_customers[name]['orders']} orders with us.")
            return name, points, True
        else:
            print(f"\n👋 Hi {name}! You're not registered as a VIP customer.")
            print("We'll register you automatically after your order.")
            return name, 0, False
    else:
        print("\n👋 Welcome, new customer!")
        name = input("What's your name? ")
        print(f"    Thanks {name}, we'll register you after the order.")
        return name, 0, False


def show_main_menu():
    """Displays the main options menu."""
    print("\n" + "=" * 40)
    print("        MAIN MENU")
    print("=" * 40)
    print("1. 📖 View full menu")
    print("2. 🛒 Place an order")
    print("3. 🎁 View today's offers")
    print("4. ⭐ Redeem points")
    print("5. 🚪 Exit")
    print("=" * 40)


def show_full_menu():
    """Displays all available products organized by category."""
    print("\n" + "=" * 50)
    print("           FULL MENU")
    print("=" * 50)

    # Iterate over each menu category
    for category in menu:
        print(f"\n🍴 {category}")
        print("-" * 30)

        counter = 1
        products = menu[category]
        for name in products:
            info = products[name]
            price = info["price"]
            time = info["time"]
            points = info["points"]
            print(f"  {counter}. {name}")
            print(f"     💵 ${price:.2f} | ⏱️ {time} min | ⭐ {points} pts")
            counter += 1

    print("\n" + "=" * 50)
    input("\nPress Enter to continue...")


def show_offers():
    """Displays the special combos of the day."""
    print("\n" + "=" * 50)
    print("        🎁 TODAY'S OFFERS 🎁")
    print("=" * 50)

    counter = 1
    for combo_name in daily_combos:
        combo_info = daily_combos[combo_name]
        products = ""
        for item in combo_info['items']:
            products += f'{item}, '
        print(f"\n{counter}. {combo_name}")
        print(f"   Includes: {products[:-2]}")
        print(f"   💥 {combo_info['discount']}% discount")
        counter += 1

    print("\n" + "=" * 50)
    input("\nPress Enter to continue...")


def calculate_price_with_points(total, available_points):
    """
    Asks whether the customer wants to use their points and calculates the discount.

    Args:
        total (float): Order total
        available_points (int): Customer's available points

    Returns:
        tuple: (new_total, points_used)
    """
    if available_points == 0:
        return total, 0

    # Conversion: 100 points = $1
    max_discount = available_points / 100

    print(f"\n💰 You have {available_points} available points")
    print(f"   That's worth up to ${max_discount:.2f} in discount")

    use_points = ""
    while use_points not in ["y", "n", "yes", "no"]:
        use_points = input("Do you want to use your points? (y/n): ")
        if use_points not in ["y", "n", "yes", "no"]:
            print("❌ Please enter 'y' or 'n'")

    if use_points in ["y", "yes"]:
        points_to_use = 0
        while True:
            entry = input(f"How many points do you want to use? (max {available_points}): ")

            # Check that it's a number
            is_number = True
            for char in entry:
                if char not in "0123456789":
                    is_number = False
                    break

            if is_number and entry != "":
                points_to_use = int(entry)
                if 0 <= points_to_use <= available_points:
                    discount = points_to_use / 100
                    if discount <= total:
                        return total - discount, points_to_use
                    else:
                        print(f"❌ The discount (${discount:.2f}) is greater than the total")
                else:
                    print(f"❌ You must enter a number between 0 and {available_points}")
            else:
                print("❌ Please enter a valid number")

    return total, 0



def check_combo(order_items):
    """
    Checks whether the items in the order form any combo.

    Args:
        order_items (list): List of product names in the order.

    Returns:
        tuple: (combo_name, discount) or (None, 0) if there is no combo
    """
    for combo_name in daily_combos:
        combo_info = daily_combos[combo_name]
        # Check whether all combo items are in the order
        if all(item in order_items for item in combo_info["items"]):
            return combo_name, combo_info["discount"]

    return None, 0


def place_order(customer_name, available_points):
    """
    Main process for placing an order.

    Args:
        customer_name (str): Customer's name
        available_points (int): Customer's available points

    Returns:
        tuple: (final_total, points_earned, points_used)
    """
    cart = []  # List of tuples (product, quantity, unit_price, time)
    keep_going = True

    while keep_going:
        print("\n" + "=" * 40)
        print("        PLACE AN ORDER")
        print("=" * 40)
        print("1. Appetizers")
        print("2. Main Courses")
        print("3. Desserts")
        print("4. Drinks")
        print("5. View cart")
        print("6. Finish order")
        print("=" * 40)

        option = input("\nChoose an option: ")

        if option == "1":
            add_product(cart, "appetizers")
        elif option == "2":
            add_product(cart, "main_courses")
        elif option == "3":
            add_product(cart, "desserts")
        elif option == "4":
            add_product(cart, "drinks")
        elif option == "5":
            show_cart(cart)
        elif option == "6":
            if len(cart) > 0:
                keep_going = False
            else:
                print("\n❌ The cart is empty. Add products before finishing.")
        else:
            print("\n❌ Invalid option. Try again.")

    # Calculate totals and apply discounts
    return process_order(cart, customer_name, available_points)


def add_product(cart, category):
    """
    Adds a product to the cart from a specific category.

    Args:
        cart (list): Shopping cart list
        category (str): Menu category
    """
    print(f"\n--- {category} ---")
    products = menu[category]

    # Show the products in the category
    product_list = []
    counter = 1
    for name in products:
        info = products[name]
        print(f"{counter}. {name} - ${info['price']:.2f}")
        product_list += [(name, info)]
        counter += 1
    print("0. Go back")

    # Select a product
    selection = input("\nWhat would you like to add? (0 to go back): ")

    # Validate input
    is_number = True
    for char in selection:
        if char not in "0123456789":
            is_number = False
            break

    if not is_number or selection == "":
        print("❌ Please enter a valid number.")
        return

    selection = int(selection)

    if selection == 0:
        return

    elif 1 <= selection <= len(product_list):
        product_name, product_info = product_list[selection - 1]

        # Ask for the quantity
        quantity_str = input("How many units? ")

        # Validate the quantity
        is_number = True
        for char in quantity_str:
            if char not in "0123456789":
                is_number = False
                break

        if is_number and quantity_str != "" and int(quantity_str) > 0:
            quantity = int(quantity_str)
            # Add to cart (name, quantity, unit_price, time, points)
            cart += [(
                product_name,
                quantity,
                product_info["price"],
                product_info["time"],
                product_info["points"]
            )]
            print(f"\n✅ {quantity}x {product_name} added to cart")
        else:
            print("❌ Invalid quantity.")
    else:
        print("❌ Invalid selection.")


def show_cart(cart):
    """
    Displays the current contents of the cart.

    Args:
        cart (list): Shopping cart list
    """
    if len(cart) == 0:
        print("\n🛒 The cart is empty.")
        input("\nPress Enter to continue...")
        return

    print("\n" + "=" * 50)
    print("           🛒 YOUR CART")
    print("=" * 50)

    total = 0
    total_time = 0

    for item in cart:
        name, quantity, price, time, points = item
        subtotal = quantity * price
        total += subtotal
        total_time = max(total_time, time)

        print(f"{quantity}x {name}")
        print(f"   ${price:.2f} each = ${subtotal:.2f}")

    print("-" * 50)
    print(f"TOTAL: ${total:.2f}")
    print(f"Estimated time: {total_time} minutes")
    print("=" * 50)

    input("\nPress Enter to continue...")


def process_order(cart, customer_name, available_points):
    """
    Processes the final order, applying discounts and calculating points.

    Args:
        cart (list): Shopping cart list
        customer_name (str): Customer's name
        available_points (int): Customer's available points

    Returns:
        tuple: (final_total, points_earned, points_used)
    """
    # Calculate initial totals
    subtotal = 0
    max_time = 0
    points_earned = 0
    order_items = []

    print("\n" + "=" * 60)
    print("           📋 ORDER SUMMARY")
    print("=" * 60)

    for item in cart:
        name, quantity, price, time, points = item
        item_subtotal = quantity * price
        subtotal += item_subtotal
        points_earned += points * quantity
        max_time = max(max_time, time)

        # Add items to the list to check for combos
        for _ in range(quantity):
            order_items += [name]

        print(f"{quantity}x {name}: ${item_subtotal:.2f}")

    print("-" * 60)
    print(f"Subtotal: ${subtotal:.2f}")

    # Check whether there's a combo
    applied_combo, combo_discount = check_combo(order_items)
    discount_amount = 0

    if applied_combo:
        discount_amount = subtotal * (combo_discount / 100)
        print(f"\n🎉 {applied_combo} applied!")
        print(f"   {combo_discount}% discount: -${discount_amount:.2f}")

    total = subtotal - discount_amount

    # Apply points discount if the customer wants to
    points_used = 0
    if available_points > 0:
        total, points_used = calculate_price_with_points(total, available_points)
        if points_used > 0:
            print(f"⭐ Points used: {points_used} (-${points_used/100:.2f})")

    # Happy Hour: additional 10% discount (simulated with order number)
    orders_today = 47  # Fixed number to simulate today's orders
    if orders_today % 10 == 7:  # Every 10 orders, the 7th gets happy hour
        happy_hour_discount = total * 0.10
        print(f"\n🍻 HAPPY HOUR! Additional 10% discount: -${happy_hour_discount:.2f}")
        total -= happy_hour_discount

    # Surprise customer (every 50th order)
    if orders_today == 50:
        print("\n🎊 CONGRATULATIONS! You're our 50th customer of the day!")
        print("   Your order is FREE! 🎁")
        total = 0

    print("\n" + "=" * 60)
    print(f"TOTAL TO PAY: ${total:.2f}")
    print(f"Delivery time: {max_time} minutes")
    print(f"Points earned: {points_earned}")
    print("=" * 60)

    # Confirm order
    confirm = ""
    while confirm not in ["y", "n", "yes", "no"]:
        confirm = input("\nConfirm order? (y/n): ")
        if confirm not in ["y", "n", "yes", "no"]:
            print("❌ Please enter 'y' or 'n'")

    if confirm in ["y", "yes"]:
        print("\n✅ Order confirmed!")
        print(f"📍 Your order will arrive in {max_time} minutes.")

        # Ask for a review
        print("\n⭐ How would you rate your experience? (1-5 stars)")
        rating = input("Rating: ")

        # Validate rating
        if rating in ["1", "2", "3", "4", "5"]:
            stars = "⭐" * int(rating)
            print(f"\nThanks for your {stars} rating!")

        # Register customer
        if customer_name not in vip_customers:
            vip_customers[customer_name] = {"points": points_earned, "orders": 1}
            print(f"\nYou've been registered as a VIP customer, log in with your name!")

        return total, points_earned, points_used
    else:
        print("\n❌ Order cancelled.")
        return 0, 0, 0


def main():
    """Main function of the program"""
    # Show welcome message
    show_welcome()

    # Verify the customer
    customer_name, available_points, is_vip = verify_customer()

    # Variables to control the program
    running = True
    total_points_earned = 0
    total_points_used = 0

    # Main program loop
    while running:
        show_main_menu()
        option = input("\nChoose an option: ")

        if option == "1":
            # View full menu
            show_full_menu()

        elif option == "2":
            # Place an order
            total, points_earned, points_used = place_order(
                customer_name,
                available_points
            )
            total_points_earned += points_earned
            total_points_used += points_used
            is_vip = True

        elif option == "3":
            # View offers
            show_offers()

        elif option == "4":
            # Redeem points
            pass

        elif option == "5":
            # Exit
            print("\n" + "=" * 50)
            print("Thanks for visiting us! 👋")
            print(f"See you soon, {customer_name}!")

            # Show summary if there was activity
            if total_points_earned > 0 or total_points_used > 0:
                print("\nYour session summary:")
                print(f"  Points earned: {total_points_earned}")
                print(f"  Points used: {total_points_used}")
                final_balance = available_points - total_points_used + total_points_earned
                print(f"  Points balance: {final_balance}")

            print("=" * 50)
            running = False

        else:
            print("\n❌ Invalid option. Please choose between 1 and 5.")

    print("\nProgram finished!")


# ===== RUN THE PROGRAM =====
# Call the main function
main()
