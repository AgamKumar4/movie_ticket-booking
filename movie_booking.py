print("================================")
print("       AVAILABLE MOVIES")
print("================================")

movies = [
    ["Avengers: Endgame", "Action", ["10:00 AM", "2:00 PM", "6:00 PM"], 150],
    ["3 Idiots", "Comedy", ["11:00 AM", "3:00 PM", "7:00 PM"], 120],
    ["Interstellar", "Sci-Fi", ["9:00 AM", "1:00 PM", "5:00 PM"], 180],
    ["Dangal", "Sports", ["10:30 AM", "2:30 PM", "6:30 PM"], 130]
]

for i in range(len(movies)):
    print(i + 1, ".", movies[i][0])
print()
choice = int(input("Enter the movie number: "))

if choice >= 1 and choice <= len(movies):
    selected_movie = movies[choice - 1]

    print("Movie:", selected_movie[0])
    print("Genre:", selected_movie[1])
    print("Show Timings:")

    for i in range(len(selected_movie[2])):
        print(i + 1, ".", selected_movie[2][i])

    print("Ticket Price: ₹", selected_movie[3])

else:
    print("Invalid movie number.")
print()
timing_choice = int(input("Enter the show timing number: "))

if timing_choice >= 1 and timing_choice <= len(selected_movie[2]):
    selected_timing = selected_movie[2][timing_choice - 1]
    print("Selected Show:", selected_timing)
    print("Ticket Price: ₹", selected_movie[3])
else:
    print("Invalid timing number.")
print()
available_seats = 40

print("Available Seats:", available_seats)

number_of_seats = int(input("Enter number of seats you want to book: "))

if number_of_seats > 0 and number_of_seats <= available_seats:
    total_amount = number_of_seats * selected_movie[3]
    available_seats = available_seats - number_of_seats

    print("Seats booked:", number_of_seats)
    print("Total Amount: ₹", total_amount)
    print("Remaining Seats:", available_seats)

else:
    print("Invalid number of seats.")
print()
name = input("Enter customer name: ")
phone = input("Enter phone number: ")

print("Customer Details")
print("Name:", name)
print("Phone:", phone)


booking_id = "MOV" + str(1000 + choice)

print("================================")
print("       BOOKING CONFIRMED")
print("================================")
print("Booking ID:", booking_id)
print("Customer Name:", name)
print("Phone:", phone)
print("Movie:", selected_movie[0])
print("Show:", selected_timing)
print("Seats:", number_of_seats)
print("Total Amount: ₹", total_amount)
print("================================")
print()
booking = {
    "booking_id": booking_id,
    "name": name,
    "phone": phone,
    "movie": selected_movie[0],
    "timing": selected_timing,
    "seats": number_of_seats,
    "amount": total_amount
}

print("Booking saved successfully!")
search_id = input("Enter Booking ID: ")

if search_id == booking["booking_id"]:

    print("================================")
    print("         BOOKING DETAILS")
    print("================================")
    print("Booking ID:", booking["booking_id"])
    print("Customer Name:", booking["name"])
    print("Phone:", booking["phone"])
    print("Movie:", booking["movie"])
    print("Show:", booking["timing"])
    print("Seats:", booking["seats"])
    print("Total Amount: ₹", booking["amount"])
    print("================================")

else:
    print("Booking ID not found.")
print()
cancel_id = input("Enter Booking ID to cancel: ")

if cancel_id == booking["booking_id"]:

    print("Booking found!")
    print("Movie:", booking["movie"])
    print("Seats:", booking["seats"])

    confirm = input("Do you want to cancel this booking? (yes/no): ")

    if confirm.lower() == "yes":
        available_seats = available_seats + booking["seats"]

        print("Booking cancelled successfully!")
        print("Seats returned:", booking["seats"])
        print("Available Seats:", available_seats)

        booking = {}

    else:
        print("Booking cancellation stopped.")

else:
    print("Booking ID not found.")
    

