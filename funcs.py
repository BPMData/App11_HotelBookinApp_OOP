from fpdf import FPDF
from datetime import datetime
import pandas as pd


df = pd.read_csv("articles.csv")
pdf = FPDF(orientation="portrait", unit="mm", format="A4")


def get_minion(pdf):
    pdf.add_font(family="Minion", fname="C:\Fonts\Minion\TTF\MinionProReg.ttf",
                 uni=True)

    pdf.add_font(family="MinionItal", fname="C:\Fonts\Minion\TTF\MinionProItal.ttf",
                 uni=True)

    pdf.add_font(family="MinionBold", fname="C:\Fonts\Minion\TTF\MinionProBold.ttf",
                 uni=True)

    pdf.add_font(family="MinionBoldItal", fname="C:\Fonts\Minion\TTF\MinionProBoldItal.ttf",
                 uni=True)

    pdf.add_font(family="MinionImpact", fname="C:\Fonts\Minion\TTF\MinionProBigBold.ttf",
                 uni=True)

    pdf.add_font(family="MinionImpactItal", fname="C:\Fonts\Minion\TTF\MinionProBigBoldItal.ttf",
                 uni=True)


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
