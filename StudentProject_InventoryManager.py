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
from funcs import get_minion, Inventory, Receipt, df


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