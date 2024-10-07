"""
Periodic Table of Elements
Author: Al Sweigart, al@inventwithpython.com

This program allows you to display the periodic table of elements and obtain detailed
information about a chosen element by providing its symbol or atomic number.

Instructions:
- Enter the symbol or atomic number to get information about the selected element.
- Type 'EXIT' to end the program.

Code downloaded from: https://ftp.helion.pl/przyklady/wiksma.zip.
Tags: short, science
"""
import csv

elements = []
with open('periodictable.csv', mode='r', encoding='iso-8859-2') as file:
    reader = csv.reader(file)

    for row in reader:
        elements.append(row)


def show_element_details(number):
    print("****")
    print("User choose: ", number)
    
    # if 1 <= number <= len(elements):
    #     element = elements[number - 1]
    #     print(f"Pierwiastek {element[1]} (Symbol: {element[2]})")
    #     print(f"Liczba atomowa: {element[0]}")
    #     print(f"Masa atomowa: {element[3]}")
    #     print(f"Grupa: {element[4]}, Okres: {element[5]}")
    # else:
    #     print("Liczba poza zakresem. Podaj liczbę między 1 a", len(elements))


def show_element_options():
    print("Available elements")
    for element in elements:
        if len(element) >= 3:
            print(f"{element[2]} - {element[1]}")

while True:
    show_element_options()
    user_input = input("Enter the symbol or atomic number to get more information about the element, or END to exit the program. ")

    if user_input.lower() == 'end':
        print("Goodbye!")
        break

    try:
        number = int(user_input)
        show_element_details(number)
    except ValueError:
        print("I'm sorry, I didn't understand. Please try again. Please enter a number or 'END")