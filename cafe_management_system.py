from datetime import datetime

# Menu of the cafe
menu = {
    'Pizza': 200,
    'Pasta': 120,
    'Burger': 50,
    'Chowmin': 100,
    'Maggie': 70,
    'Sandwich': 100,
    'Coffee': 80,
    'Shakes': 100,
}

def show_menu():
    print("\n----- CODE & COFFEE CAFE MENU -----")
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")
    print("------------------------------------")

def take_order():
    order = {}
    order_total = 0

    while True:
        item = input("Enter item name to order (or type 'done' to finish): ").strip().title()

        if item.lower() == 'done':
            break

        if item in menu:
            qty = int(input(f"Enter quantity for {item}: "))
            order[item] = order.get(item, 0) + qty
            order_total += menu[item] * qty
            print(f"Added {qty} x {item} to your order.")
        else:
            print(f"Sorry, '{item}' is not available on the menu.")

    return order, order_total

def generate_bill(order, order_total):
    print("\n========= BILL =========")
    for item, qty in order.items():
        print(f"{item} x{qty} = Rs.{menu[item] * qty}")
    print(f"-------------------------")
    print(f"Total Amount: Rs.{order_total}")
    print("=========================\n")

def save_order_to_file(order, order_total):
    with open("orders.txt", "a") as f:
        f.write(f"\n--- Order at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        for item, qty in order.items():
            f.write(f"{item} x{qty} = Rs.{menu[item] * qty}\n")
        f.write(f"Total: Rs.{order_total}\n")

def main():
    print("Welcome to CODE & COFFEE CAFE")
    show_menu()

    order, order_total = take_order()

    if order:
        generate_bill(order, order_total)
        save_order_to_file(order, order_total)
        print("Order saved successfully. Thank you for visiting!")
    else:
        print("No items ordered. Goodbye!")

if __name__ == "__main__":
    main()