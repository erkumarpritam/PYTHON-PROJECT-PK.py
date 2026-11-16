Bus/Train Ticket Booking System 🚆
A lightweight, robust, and console-based Bus/Train Ticket Booking System written in Python 3. This project simulates a real-time reservation management workflow, allowing users to view seats, book tickets, track passenger details, and handle cancellations efficiently.
🚀 Key Features
View Seats: Displays real-time availability, listing free seats, total remaining capacity, and currently booked seats.
Book Seat: Prompts for seat numbers (1 to 10) and passenger names, featuring built-in validation against double-bookings and out-of-range inputs.
View Bookings: Renders an organized view of all active reservations mapped to their respective passengers.
Cancel Booking: Processes ticket cancellations, frees up seats, and automatically computes an 80% refund policy (Rs. 400 from the standard Rs. 500 fare).
💻 Programming Concepts & Technologies Used
Language: Python 3 (Clean procedural design).
Data Structures:
Lists: Used to maintain the static inventory of seats (1 to 10).
Dictionaries: Acts as a key-value store (seat_number: passenger_name) for fast lookups and record management.
Control Flow & Functions: Utilizes continuous while loops, conditional branching (if-elif-else), and modular functions (view_seats, book_seat, cancel_booking) to keep code clean and maintainable.
Error Handling: Implements try-except blocks to prevent application crashes from unexpected inputs (e.g., entering text instead of numbers).
⚙️ How to Run
