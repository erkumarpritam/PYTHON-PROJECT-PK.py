"""
Project Title: Bus/Train Ticket Booking System
Language: Python 3
Description: A console-based ticket booking application implementing seat management,
             passenger records, fare calculations, and cancellation refunds.
"""

def display_menu():
    """Displays the main application menu."""
    print("\n========================================")
    print("      BUS / TRAIN TICKET BOOKING SYSTEM")
    print("========================================")
    print("1. View Seats")
    print("2. Book Seat")
    print("3. View Bookings")
    print("4. Cancel Booking")
    print("5. Exit")
    print("----------------------------------------")

def view_seats(seats, bookings):
    """Option 1: Display available and booked seats, and total seats left."""
    print("\n--- Seat Availability Status ---")
    available_seats = [s for s in seats if s not in bookings]
    booked_seats = sorted(list(bookings.keys()))
    
    print(f"Total Seats Left: {len(available_seats)}")
    print(f"Available Seats : {available_seats}")
    print(f"Booked Seats    : {booked_seats if booked_seats else 'None'}")

def book_seat(seats, bookings):
    """Option 2: Prompt for seat number and passenger name, validate, and book."""
    print("\n--- Book a Seat ---")
    try:
        seat_input = input("Enter seat number (1 to 10): ").strip()
        seat = int(seat_input)
        
        # Validation 1: Check if seat is within valid range
        if seat not in seats:
            print("Invalid seat. Choose a seat from 1 to 10.")
            return
            
        # Validation 2: Check if seat is already booked
        if seat in bookings:
            print(f"Seat {seat} is already booked.")
            return
            
        # Validation 3: Check passenger name validity
        name = input("Enter passenger name: ").strip()
        if not name:
            print("Invalid passenger name. Name cannot be empty.")
            return
            
        # Process booking
        bookings[seat] = name
        seats_left = len(seats) - len(bookings)
        
        print(f"\nSeat {seat} booked for {name}.")
        print(f"Fare: Rs. 500")
        
        if seats_left == 0:
            print("Seats left: 0. Bus is now full.")
        else:
            print(f"Seats left: {seats_left}")
            
    except ValueError:
        print("Invalid input! Please enter a valid numeric seat number.")

def view_bookings(bookings):
    """Option 3: Display all current seat bookings and associated passenger names."""
    print("\n--- Current Seat Bookings ---")
    if not bookings:
        print("No bookings found yet.")
        return
        
    print(f"{'Seat Number':<15} | {'Passenger Name'}")
    print("-" * 35)
    for seat in sorted(bookings.keys()):
        print(f"{seat:<15} | {bookings[seat]}")

def cancel_booking(seats, bookings):
    """Option 4: Prompt for seat number, validate, process cancellation, and calculate refund."""
    print("\n--- Cancel Booking ---")
    try:
        seat_input = input("Enter seat number to cancel (1 to 10): ").strip()
        seat = int(seat_input)
        
        # Validation 1: Check if seat is within range
        if seat not in seats:
            print("Invalid seat. Choose a seat from 1 to 10.")
            return
            
        # Validation 2: Check if seat is actually booked
        if seat not in bookings:
            print(f"Seat {seat} is not currently booked.")
            return
            
        # Process cancellation and refund (80% of Rs. 500 = Rs. 400)
        passenger = bookings.pop(seat)
        refund_amount = int(500 * 0.80)
        
        print(f"Booking for seat {seat} cancelled.")
        print(f"Refund: Rs. {refund_amount}")
        
    except ValueError:
        print("Invalid input! Please enter a valid numeric seat number.")

def main():
    """Main program execution loop."""
    # Data structures as required
    seats = list(range(1, 11))  # List containing seats 1 to 10
    bookings = {}               # Dictionary mapping seat numbers to passenger names
    
    print("Welcome to the Ticket Booking System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_seats(seats, bookings)
        elif choice == '2':
            book_seat(seats, bookings)
        elif choice == '3':
            view_bookings(bookings)
        elif choice == '4':
            cancel_booking(seats, bookings)
        elif choice == '5':
            print("\nThank you for using the Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid menu choice! Please select an option from 1 to 5.")

if __name__ == "__main__":
    main()