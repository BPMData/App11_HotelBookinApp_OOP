"""
Intended functionality:

User can query current inventory db
User can choose an inventory item and a quantity
Receipt is generated for cost of items, quantity of item selected removed from inventory db
"""


# ok

"""
Needed classes:

database class
receipt class
"""
from funcs import get_minion
import pandas as pd
from fpdf import FPDF
from datetime import datetime

df = pd.read_csv("articles.csv")


class Inventory:
    def __init__(self, item, quantity):
        self.item_id = item
        self.quantity = quantity
        self.current_stock = df.loc[df['id'] == self.item_id, "stock"].squeeze()
        self.receipt_number = df.loc[df['name'] == 'receipt_number', "stock"].squeeze()

    def save_changes(self):
        df.loc[df['id'] == self.item_id, "stock"] = self.current_stock - self.quantity
        df.to_csv('articles.csv', index=False)


class Receipt:
    def __init__(self, item, quantity):
        self.item_id = item
        self.quantity = quantity
        self.price = df.loc[df['id'] == self.item_id, "price"].squeeze()
        self.item_name = df.loc[df['id'] == self.item_id, "name"].squeeze()
        self.receipt_number = df.loc[df['name'] == 'receipt_number',"stock"].squeeze()
        self.total = self.quantity * self.price

    def generate(self, item, quantity):
        # Get current date and time
        now = datetime.now()

        # Format date and time
        formatted_now = now.strftime("%B %d, %Y, %I:%M %p")

        pdf = FPDF(orientation="p", unit="mm", format="A4")
        get_minion(pdf)
        pdf.add_page()
        pdf.set_font(family="MinionBold", size=16)
        pdf.cell(w=50, h=8, txt="Receipt #" + str(self.receipt_number), ln=1)

        # Create table
        headers = ["Item ID", "Item Name", "Item Price", "Total Cost"]
        pdf.set_fill_color(178, 255, 255)  # Celeste. Thanks https://rgbcolorcode.com/color/B3FFFF
        pdf.set_text_color(255, 80, 80) # "Tomato". Going up actually makes a color lighter.
        pdf.cell(w=40, h=8, txt=headers[0], border=1, fill=True, align="C")
        pdf.cell(w=70, h=8, txt=headers[1], border=1, fill=True, align="C")
        pdf.cell(w=40, h=8, txt=headers[2], border=1, fill=True, align="C")
        pdf.cell(w=50, h=8, txt=headers[3], border=1, ln=1, fill=True, align="C")
        # input actual numbers
        pdf.set_font(family="Minion", size=12)
        pdf.cell(w=40, h=8, txt=str(self.item_id), border=1, align="C", fill=True)
        pdf.cell(w=70, h=8, txt=str(self.item_name), border=1, align="C", fill=True)
        pdf.cell(w=40, h=8, txt=str(self.price), border=1, align="C", fill=True)
        pdf.set_text_color(255, 60, 60)
        pdf.set_font(family="MinionBold", size=12)
        pdf.cell(w=50, h=8, txt=str(self.total), border=1, ln=1, align="C", fill=True)
        pdf.ln(15)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=50, txt=f"Receipt was generated on {formatted_now}.", align="L")
        pdf.output(f"receipt_{self.receipt_number}.pdf")
        df.loc[df['name'] == 'receipt_number', "stock"] = self.receipt_number + 1


while True:
    print(df)
    item = int(input("Please enter the item ID of the item you'd like to purchase: "))
    quantity = int(input("Please enter how many of this item you'd like to purchase: "))

    user_receipt = Receipt(item, quantity)
    total = user_receipt.total

    doublecheck = input(f"Your total will be ${total} for {quantity} of {user_receipt.item_name}. Would you like to continue? Please type Y or N: ").upper()

    if doublecheck == "Y":
        user_receipt.generate(item, quantity)
        print("User receipt generated as a PDF.")
        inv = Inventory(item, quantity)
        inv.save_changes()
        print("Inventory updated. Have a nice day.")
    else:
        continue