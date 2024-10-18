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


main_symbol = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
    'Cs', 'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
    'Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',
    'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Th', 'Pa', 'U', 'Np',
    'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'
]
elements = []

with open('table.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        elements.append(row)


def show_element_details(symbol_user):
    symbol_user = symbol_user.capitalize()
    for element in elements:
        if element[2].capitalize() == symbol_user:
            print("****")
            print(f"Element: {element[1]} (Symbol: {element[2]})")
            print(f"Atomic Number: {element[0]}")
            print(f"Atomic Mass: {element[3]}")
            print(f"Group: {element[4]}, Period: {element[5]}")
            print("****")
            return
    print(f"Element with symbol '{symbol_user}' not found.")


def show_element_options():
    print(
        '''            
                    Periodic table of elements

      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
            '''
            )



while True:
    show_element_options()

    user_input = input("Enter the symbol to get more information about the element, or END to exit the program ")

    if user_input.lower() == 'end':
        print("Goodbye!")
        break

    try:
        if user_input.upper() in [symbol.upper() for symbol in main_symbol]:
            show_element_details(user_input)
            
            while True:
                try_again = input("Do you want to try another element? (yes/no): ").strip().lower()

                if try_again == 'yes':
                    break

                elif try_again == 'no':
                    print("Goodbye!")
                    exit()

                else:
                    print("Please enter a valid response ('yes' or 'no').")
            
                
        else:
            print("I'm sorry, I didn't understand. Please try again. Please enter the symbol or 'END")

    except ValueError:
        print("I'm sorry, I didn't understand. Please try again. Please enter the symbol or 'END")
