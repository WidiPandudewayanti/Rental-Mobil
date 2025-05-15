# Rental-Mobil
Capstone project Purwadhika JCDS

Rental Mobil - Terminal Based Application
Preface
The Rental Mobil application is a terminal-based car rental management tool built in Python. This program is designed as a learning project to practice Python concepts including data structures, control flow, user interaction, and modular coding. The goal is to create a functional, simple application to simulate how a rental car agency would handle its vehicle inventory and rental operations.
Introduction
Rental Mobil is suitable for small-scale rental operations and educational purposes. It allows users to manage a list of cars, handle car rental and return processes, and perform CRUD operations (Create, Read, Update, Delete) on each car record. The application runs in the terminal and utilizes the `tabulate` library for clean, readable output.
Features
Feature Summary Table:

Feature	View	Create	Update	Delete	Rental Status
Cars	✅	✅	✅	✅	✅ (Sewa & Kembali)
Search	✅	-	-	-	-

View
Users can view the list of all cars in a tabular format using the tabulate library. Each car displays information such as code, brand, year, color, rental price per day, and status (Available or Rented).
Create
This feature allows users to add a new car to the system. Users will be prompted to enter values for each attribute (code, brand, year, color, price, status). The input is validated using a try-except block to prevent invalid data entry, such as non-numeric values for year or price.

Why use try-except?
- Prevents crash when user inputs incorrect type (e.g., string instead of integer).
- Validates specific status values ('Tersedia' or 'Disewa').
- Provides user-friendly error messages and exits input sequence gracefully.
Update
Users can update the details of an existing car by entering its code. They may choose which attributes to update. If a field is left blank, the existing value remains unchanged. This ensures flexibility while preserving valid data.
Delete
The delete feature allows users to remove a car from the system using its code. Confirmation is required before deletion to prevent accidental data loss.
Rental / Return
Users can mark a car as 'Disewa' (Rented) or 'Tersedia' (Available) using the Sewa and Kembalikan options. The system checks the current status to prevent redundant operations (e.g., renting an already rented car).
Search
The Cari Mobil (Search) function enables users to find cars by brand or year. It uses dictionary comprehension to efficiently filter matching entries based on partial keyword matches.

Why use dictionary comprehension?
- Concise and readable code.
- Efficient data filtering in a single expression.
- Ideal for creating a filtered dictionary of results without needing intermediate variables.
Technology
Python – Core language used for the entire application logic.
Tabulate – External library for table rendering.
Installation
Make sure Python is installed on your system.

1. Copy the Python script file (rental_mobil.py) into your working directory.
2. Install tabulate:
   pip install tabulate
3. Run the script:
   python rental_mobil.py
