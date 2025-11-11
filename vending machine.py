class Beverage:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.quantity} left)"


class VendingMachine:
    def __init__(self):
        # Initialize the vending machine with 6 beverages
        self.beverages = {
            1: Beverage("Coca-Cola", 3.50, 5),
            2: Beverage("Diet Coke", 3.50, 5),
            3: Beverage("Water", 2.50, 5),
            4: Beverage("Coffee", 4.00, 5),
            5: Beverage("Tea", 2.75, 5),
            6: Beverage("Red Bull", 5.50, 0)
        }

    def display_menu(self):
        print("\nWelcome to the Smart Vending Machine!")
        print("=====================================")
        for key, beverage in self.beverages.items():
            print(f"{key}. {beverage}")
        print("=====================================")

    def vend(self, choice, money_inserted):
        beverage = self.beverages.get(choice)
        if not beverage:
            print("Invalid selection. Please try again.")
            return money_inserted  # return money if invalid

        if beverage.quantity <= 0:
            print(f"Sorry, {beverage.name} is sold out.")
            return money_inserted  # return money if sold out

        if money_inserted < beverage.price:
            print(f"Not enough money. {beverage.name} costs ${beverage.price:.2f}.")
            print(f"You still owe ${beverage.price - money_inserted:.2f}.")
            return money_inserted  # user can add more later


        beverage.quantity -= 1
        change = money_inserted - beverage.price
        print(f"Vending your {beverage.name}...")
        if change > 0:
            print(f"Your change is ${change:.2f}.")
        print("Enjoy your drink! 🥤")
        return 0  # all money used or returned as change

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Select a beverage (1-6): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            try:
                money = float(input("Insert money: $"))
            except ValueError:
                print("Please insert a valid amount.")
                continue


            remaining_money = self.vend(choice, money)

            beverage = self.beverages.get(choice)
            while beverage and remaining_money < beverage.price and beverage.quantity > 0:
                try:
                    more = float(input("Add more money: $"))
                    remaining_money += more
                    remaining_money = self.vend(choice, remaining_money)
                except ValueError:
                    print("Please insert a valid amount.")

            input("\nPress Enter to continue...")  # Wait before showing menu again


if __name__ == "__main__":
    machine = VendingMachine()
    machine.run()