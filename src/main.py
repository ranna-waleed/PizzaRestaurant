from pizza import PizzaFactory
from toppings import Cheese, Olives, Mushrooms
from inventory_manager import InventoryManager
from payment import PayPalPayment, CreditCardPayment

def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        pizza = PizzaFactory.create_pizza(pizza_choice)
        if not pizza:
            print("Invalid choice, please try again.")
            continue

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1":
                pizza = Cheese(pizza)
            elif topping_choice == "2":
                pizza = Olives(pizza)
            elif topping_choice == "3":
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_method = PayPalPayment()
        elif payment_choice == "2":
            payment_method = CreditCardPayment()
        else:
            print("Invalid payment method.")
            continue

        payment_method.pay(pizza.get_cost())

        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())

if __name__ == "__main__":
    main()