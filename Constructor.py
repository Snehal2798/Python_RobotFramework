# 1. Create the Ticket class
class Ticket:
    # 2. Use the constructor to initialize attributes automatically
    def __init__(self, movie_name, show_time, seat_number, user_name):
        self.movie_name = movie_name
        self.show_time = show_time
        self.seat_number = seat_number
        self.user_name = user_name
        print(f"🎟️ Ticket generated for {self.user_name}!")

    # Method to display the ticket details
    def show_ticket_details(self):
        print(f"\n--- MOVIE TICKET ---")
        print(f"Customer: {self.user_name}")
        print(f"Movie:    {self.movie_name}")
        print(f"Time:     {self.show_time}")
        print(f"Seat:     {self.seat_number}")
        print("-" * 20)

# 3. Create multiple ticket objects
# The constructor runs the moment these lines are executed
ticket1 = Ticket("Inception", "19:00", "A12", "Alex Rivera")
ticket2 = Ticket("The Batman", "21:30", "F05", "Samantha Lee")

# 4. Display the details
ticket1.show_ticket_details()
ticket2.show_ticket_details()