import pandas
from abc import ABC, abstractmethod
df = pandas.read_csv("hotels.csv", dtype={"id": str})
class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass # Basically telling other programmers/yourself that every child of the abstract class Ticket must have its own
        # generate() method, which has to be defined within each child.


class Hotel:
    # Here's a class VARIABLE
    watermark = "The Real Estate Company"
    # Here's a class METHOD

    @classmethod
    def get_hotel_count(cls, df):
        return len(df)

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def __eq__(self, other): # This is redefining how == works when dealing with Hotel objects.
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert_to_euros(amount):
        amount *= 0.9
        return amount

    @staticmethod
    def convert_to_dollars(amount):
        amount *= 1.11
        return amount