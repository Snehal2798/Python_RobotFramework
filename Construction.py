#construction -You’re building a system for an online movie ticket booking app. Every time a user books a ticket, the system should store information like:
#Movie name
#Show time
#Seat number
#User name
#Whenever a ticket is created, these details should be initialized automatically using a constructor.
#Your job is to create a class called Ticket, and use a constructor (__init__ method in Python) to initialize ticket details when a new object is created.
#Objective
#Create a class with a constructor.
#Use the constructor to initialize object attributes.
#Create multiple ticket objects and display their details.


class Ticket:
    # Constructor (runs automatically when an object is created)
    def __init__(self, movie_name, show_time, seat_number, user_name):
        self.movie_name = movie_name
        self.show_time = show_time
        self.seat_number = seat_number
        self.user_name = user_name

    def display_details(self):
        print("----- Ticket Details -----")
        print(f"Movie Name : {self.movie_name}")
        print(f"Show Time  : {self.show_time}")
        print(f"Seat No.   : {self.seat_number}")
        print(f"User Name  : {self.user_name}")
        print("--------------------------")
        print()


# Creating ticket objects (constructor is called here)
ticket1 = Ticket("Avatar 3", "6:00 PM", "A10", "Snehal")
ticket2 = Ticket("Kalki 2898 AD", "9:15 PM", "B05", "Rohan")
ticket3 = Ticket("Jawan", "3:45 PM", "C22", "Aditi")

# Displaying ticket info
ticket1.display_details()
ticket2.display_details()
ticket3.display_details()