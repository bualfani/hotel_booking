import pandas as pd

df = pd.read_csv("hotels.csv")

class Hotel():
    def __init__(self, hotel_id):
        pass

    def book(self):
        pass

    def available(self):
        # checking if hotel is available
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True

class Reservation():
    def __init__(self, name, hotel):
        pass

    def generate(self):
        pass

hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your Name: ")
    reservation = Reservation(name, hotel)
    print(reservation.generate())

else:
    print("Hotel is not available")
