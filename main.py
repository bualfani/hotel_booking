import pandas as pd

df = pd.read_csv("hotels.csv")

class Hotel():
    def __init__(self):
        pass

    def book(self):
        pass

    def available(self):
        pass

class Reservation():
    def __init__(self, name, hotel):
        pass

    def generate(self):
        pass

id = input("Enter the id of the hotel: ")
hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter your Name: ")
    reservation = Reservation(name, hotel)
    print(reservation.generate())

else:
    print("Hotel is not available")
