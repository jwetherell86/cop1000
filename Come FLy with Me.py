class Seat:
    def __init__(self, number, section="Regular", price=0, is_emergency=False):
        self.number = number
        self.section = section
        self.price = price
        self.is_emergency = is_emergency
        self.taken = False

    def __str__(self):
        status = "Taken" if self.taken else "Available"
        special = " (Emergency Exit)" if self.is_emergency else ""
        return f"Seat {self.number:2d}: {self.section} - ${self.price:.2f}{special} [{status}]"


class Airplane:
    def __init__(self):
        self.seats = []
        self.total_sales = 0.0
        self.purchased_seats = []

        for i in range(1, 21):
            if i <= 4:
                # First-class seats
                self.seats.append(Seat(i, section="First Class", price=100))
            elif i in (10, 11):
                # Emergency exit seats
                self.seats.append(Seat(i, is_emergency=True))
            else:
                # Regular seats
                self.seats.append(Seat(i))

    def display_seats(self):
        print("\n==== ️ Airplane Seating Chart ====")
        for seat in self.seats:
            print(seat)
        print("=================================")

    def purchase_seat(self, seat_number):
        if seat_number < 1 or seat_number > 20:
            print(" Invalid seat number. Please choose between 1 and 20.")
            return False, 0.0

        seat = self.seats[seat_number - 1]

        if seat.taken:
            print(f" Seat {seat.number} is already taken. Choose another.")
            return False, 0.0

        # Emergency seat confirmation
        if seat.is_emergency:
            response = input(
                f" Seat {seat.number} is an emergency exit seat. "
                "You must be willing and able to assist in an emergency. (y/n): "
            ).strip().lower()
            if response != "y":
                print(" You must accept responsibility to sit in this seat.")
                return False, 0.0

        # Confirm purchase
        confirm = input(
            f"Confirm purchase of Seat {seat.number} ({seat.section}) for ${seat.price:.2f}? (y/n): "
        ).strip().lower()
        if confirm != "y":
            print(" Purchase cancelled.")
            return False, 0.0

        # Mark seat as sold
        seat.taken = True
        self.total_sales += seat.price
        self.purchased_seats.append(seat)
        print(f" Seat {seat.number} successfully purchased!")
        return True, seat.price

    def show_summary(self):
        """Show purchased seats and total."""
        if not self.purchased_seats:
            print("\n🪑 No seats have been purchased yet.")
            return

        print("\n🧾 === Purchase Summary ===")
        for seat in self.purchased_seats:
            special = " (Emergency Exit)" if seat.is_emergency else ""
            print(f"Seat {seat.number}: {seat.section}{special} - ${seat.price:.2f}")
        print(f"------------------------------")
        print(f" Total Paid: ${self.total_sales:.2f}")
        print("=============================")

    def run(self):
        print("Welcome to the Python Air Seat Booking System!")
        while True:
            self.display_seats()
            try:
                seats_to_buy = input(
                    "\nEnter seat numbers to purchase (comma-separated, or 'q' to quit): "
                ).strip()

                if seats_to_buy.lower() == "q":
                    print("Thank you for using the booking system. Goodbye!")
                    break

                seat_numbers = [int(num) for num in seats_to_buy.split(",")]

                for num in seat_numbers:
                    self.purchase_seat(num)

                # Show summary after each batch of purchases
                self.show_summary()

            except ValueError:
                print(" Please enter valid seat numbers separated by commas.")

            input("\nPress Enter to continue...")  # wait before next loop


if __name__ == "__main__":
    airplane = Airplane()
    airplane.run()