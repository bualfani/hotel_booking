import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        # Book a hotel by changing its availability to not available
        df.loc[df['id'] == self.hotel_id, 'available'] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        # checking if hotel is available
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True

class Reservation():
    def __init__(self, name, hotel):
        self.name = name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your Reservation!!
        Here is your booking information:
        Name: {self.name}
        Hotel: {self.hotel.name}
        """
        return content

class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self, expiration_date, holder, cvc):
        card_data = {"number": self.card_number, "expiration": expiration_date, "holder": holder, "cvc": cvc}
        if  card_data in df_cards:
            return True
        else:
            return False


hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(card_number='123456789', expiration_date="12/13", name="Tim Ber", cvc="123")
    if credit_card.validate():
        hotel.book()
        name = input("Enter your Name: ")
        reservation = Reservation(name, hotel)
        print(reservation.generate())

    else:
        print('There was somthing wrong with your payment method')

else:
    print("Hotel is not available")
