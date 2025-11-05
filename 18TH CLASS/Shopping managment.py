# 🛒 Shopping Cart Management System

cart = {}

def add_to_cart():
    item = input('Enter item name to add: ').strip().capitalize()
    try:
        price = float(input(f'Enter price for {item}: '))
        quantity = int(input(f'Enter quantity for {item}: '))
    except ValueError:
        print("❌ Invalid input. Please enter numbers for price and quantity.")
        return

    if item in cart:
        cart[item]['quantity'] += quantity
        cart[item]['price'] = price  # update latest price
    else:
        cart[item] = {'price': price, 'quantity': quantity}

    print(f'✅ Added {quantity} x {item} @ Rs.{price:.2f} each to cart.')


def view_cart():
    if not cart:
        print('🛍️ Your cart is empty.')
        return

    print('\n===== 🧾 Your Shopping Cart =====')
    total = 0
    for item, details in cart.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f'{item:<15} Rs.{details["price"]:<10.2f} x {details["quantity"]:<3} = Rs.{item_total:.2f}')

    print('-----------------------------------')
    print(f'Total Amount: Rs.{total:.2f}')
    print('===================================\n')


def remove_from_cart():
    if not cart:
        print("❌ Your cart is empty. Nothing to remove.")
        return

    item = input('Enter item name to remove: ').strip().capitalize()
    if item in cart:
        del cart[item]
        print(f'🗑️ Item "{item}" removed from cart.')
    else:
        print(f'❌ Item "{item}" not found in cart.')


def checkout():
    if not cart:
        print("🛍️ Your cart is empty. Nothing to checkout.")
        return

    total = sum(details['price'] * details['quantity'] for details in cart.values())
    print('\n===== 💳 Checkout Summary =====')
    for item, details in cart.items():
        print(f'{item:<15} x {details["quantity"]} = Rs.{details["price"] * details["quantity"]:.2f}')
    print('-----------------------------------')
    print(f'🧾 Grand Total: Rs.{total:.2f}')
    print('===================================')
    print('🎉 Thank you for shopping with us! Goodbye!\n')
    cart.clear()  # Empty cart after checkout


def main():
    while True:
        print('\n===== 🛒 Shopping Cart Menu =====')
        print('1️⃣  Add Item to Cart')
        print('2️⃣  View Cart')
        print('3️⃣  Remove Item from Cart')
        print('4️⃣  Checkout')
        print('5️⃣  Exit')
        print('=================================')

        choice = input('Enter your choice: ').strip()

        if choice == '1':
            add_to_cart()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            print('👋 Thank you for using the Shopping Cart System. Goodbye!')
            break
        else:
            print('❌ Invalid choice. Please try again.')


# Run the program
if __name__ == "__main__":
    main()
