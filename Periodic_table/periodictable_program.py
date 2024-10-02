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

with open('periodictable.csv', mode='r', encoding='latin1') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)

userChoice = input('Enter the symbol or atomic number to get more information about the element, or END to exit the program. ')
print(userChoice)