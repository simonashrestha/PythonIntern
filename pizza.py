pizzas = {
    "Margherita": 8.00,
    "Pepperoni": 9.00,
    "Hawaiian": 9.50,
    "Vegetarian": 10.00,
}
toppings = {
    "Pepperoni": 1.50,
    "Mushrooms": 0.75,
    "Onions": 0.50,
    "Extra Cheese": 1.00,
}
total_bill = 0.00
while True:
    print("\nOur Pizzas:")
    pizza_list = list(pizzas.items())
    for index, (pizza, price) in enumerate(pizza_list, start=1):
        print(f"{index}. {pizza}: ${price:.2f}")

    pizza_choice_num = input("\nSelect a pizza by number (or 'no' to finish): ").lower()
    if pizza_choice_num == "no":
        break
    if not pizza_choice_num.isdigit() or int(pizza_choice_num) < 1 or int(pizza_choice_num) > len(pizza_list):
        print(f"Sorry, '{pizza_choice_num}' is not a valid choice.")
        continue

    pizza_choice = pizza_list[int(pizza_choice_num) - 1][0]
    pizza_price = pizzas[pizza_choice]
    subtotal = pizza_price

    print(f"\nYou have selected {pizza_choice} for ${pizza_price:.2f}")
    print("\nToppings:")
    topping_list = list(toppings.items())
    for index, (topping, price) in enumerate(topping_list, start=1):
        print(f"{index}. {topping}: ${price:.2f}")

    add_topping = input("\nDo you want to add toppings? (yes/no): ").lower()
    if add_topping == "yes":
        while True:
            topping_choice_num = input("\nSelect a topping by number (or 'no' to finish): ").lower()
            if topping_choice_num == "no":
                break
            if not topping_choice_num.isdigit() or int(topping_choice_num) < 1 or int(topping_choice_num) > len(
                    topping_list):
                print(f"Sorry, '{topping_choice_num}' is not a valid choice.")
                continue

            topping_choice = topping_list[int(topping_choice_num) - 1][0]
            topping_price = toppings[topping_choice]
            subtotal += topping_price
            print(f"\nSubtotal for {pizza_choice} with {topping_choice}: ${subtotal:.2f}")

    total_bill += subtotal
    print(f"\nYour total bill amount: ${total_bill:.2f}")
