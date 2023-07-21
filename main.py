from source_hotel import df, ReservationTicket, Hotel, SecureCreditCard, Spa

print(df)
hotel_input = int(input("Enter the ID of the hotel: "))

hotel_booked = False

hotel = Hotel(hotel_input)
if hotel.available():
    credit = SecureCreditCard(number="1234567890123456")
    if credit.validate(expiration="12/28", holder="JANE DOE", cvc="456"):
            password = input("Please enter your password. Passwords are case sensitive: ")
            if  credit.authenticate(password):
                hotel.book()
                print("Your credit card successfully validated.")
                name = input('Enter your name: ')
                reservation = ReservationTicket(name, hotel)
                print(reservation.generate())
                hotel_booked = True
            else:
                print("The entered password was incorrect.")
    else:
        print("There was a problem with the credit card you entered.")
else:
    print("Hotel is not free.")

if hotel_booked:
    spa_decision = input("Would you like to book a spa package? Please type Y or N: ").upper()
    if spa_decision == "Y":
        spa = Spa(hotel, name)
        spa.book()
        spaticket = spa.ticketgenerate()
        print(spaticket)
        hotel_booked = False
    else:
       print("Understandable. Have a nice day.")