import pandas as pd

df = pd.read_csv("hotels.csv")
cards_data = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
cards_security = pd.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Check if the hotel is available"""
        if self.availability == 'yes':
         return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
        Thank you for your reservation, {self.customer_name}.
        You will be staying at {self.hotel.name}.
        """
        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        CARD_DATA = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if CARD_DATA in cards_data:
            return True
        else:
            return False # Though technically it will return NONE if not true which will be equivalent to FALSE for our purposes, so this line is not 100% needed

class SecureCreditCard(CreditCard): # This makes SecureCreditCard a child which inherits the abilities of the parent.

    def authenticate(self, given_password):
        password = cards_security.loc[cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

class Spa(Hotel):
    def __init__(self, hotel, customer_name):
        self.customer_name = customer_name
        self.name = hotel.name

    def book(self):
        print(f"You have booked a stay at the spa of {self.name}.")

    def ticketgenerate(self):
        content = f"""
        Thank you for your spa reservation, {self.customer_name}.
        You will be enjoying the spa at {self.name} during your stay at that hotel.
        """
        return content


