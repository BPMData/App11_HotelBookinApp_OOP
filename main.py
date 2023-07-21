import pandas as pd

df = pd.read_csv("hotels.csv")
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
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

print(df)
hotel_input = int(input("Enter the ID of the hotel: "))

hotel = Hotel(hotel_input)
if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation.generate())
else:
    print("Hotel is not free.")

1