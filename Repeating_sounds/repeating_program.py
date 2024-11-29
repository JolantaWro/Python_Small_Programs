"""
Sound Repetition
Author: Al Sweigart (al@inventwithpython.com)

A memory game with sounds, where the player must remember increasingly longer sequences of letters. 
The player has to correctly repeat the sequences generated by the program, which are both visual and auditory. 
Each new round adds another element to the sequence, increasing the level of difficulty.

The game is inspired by the popular electronic toy Simon, known for its challenges of repeating growing sequences of colors and sounds. 
This program offers a great way to exercise memory and concentration.
"""

from playsound import playsound
from random import choice
import time

def show_element_options(): 
    """Shows instructions on what key to press when hearing a specific sound."""
    # print("\n___When you hear this sound____")
    # time.sleep(2) 
    # playsound('soundA.wav')
    # time.sleep(1) 
    # print("press A")
    # print("\n___When you hear this sound___")
    # time.sleep(2) 
    # playsound('soundS.wav')
    # time.sleep(1) 
    # print("press S")
    # print("\n___When you hear this sound___")
    # time.sleep(2) 
    # playsound('soundD.wav')
    # time.sleep(1) 
    # print("press D")
    # print("\n___When you hear this sound___")
    # time.sleep(2) 
    # playsound('soundF.wav')
    # time.sleep(1) 
    # print("press F")
    sounds = {'A': 'soundA.wav', 'S': 'soundS.wav', 'D': 'soundD.wav', 'F': 'soundF.wav'}
    for key, sound in sounds.items():
        print(f"\nWhen you hear this sound:")
        playsound(sound)
        time.sleep(1)
        print(f"Press '{key}'.")

def play_sequence(sequence):
    """Play the sequence of sounds for the player to remember."""
    for element in sequence:
        if element == 'A':
            playsound('soundA.wav')
            print("A")
        elif element == 'S':
            playsound('soundS.wav')
            print("S")
        elif element == 'D':
            playsound('soundD.wav')
            print("D")
        elif element == 'F':
            playsound('soundF.wav')
            print("F")
        time.sleep(0.5)

def play_round():
    sequence = []
    round_number = 1

    new_element = choice(['A', 'F', 'D', 'S'])
    sequence.append(new_element)

print("=== Welcome to the game! ===")
while True:
    print("\nAre you ready for the game?")
    print("1. Yes, I am ready!")
    print("2. I want to listen to the sound.")
    print("3. Exit the game.")
        
    user_choice = input("Choose an option (1, 2, 3): ")

    if user_choice == '1':
        print("\nGreat! Let's start the game!")
        sequence = []
        round_number = 1
        guest_round = 0

        while True:
            print(f"\n--- Round {round_number} ---")
            new_element = choice(['A', 'F', 'D', 'S'])
            sequence.append(new_element)

            play_sequence(sequence)

            player_input = input("Repeat the sequence: ").strip().upper()
            # if player_input in sequence: 
            #     print("YES")
            #     guest_round += 1
            #     new_element = choice(['A', 'F', 'D', 'S'])
            #     sequence.append(new_element)
            #     play_sequence(sequence)
            
            # print(player_input)
            # break
            if player_input == ''.join(sequence):
                print("Correct! Get ready for the next round!")
                round_number += 1
                time.sleep(1)
                new_element = choice(['A', 'F', 'D', 'S'])
                print(new_element)
            else:
                print("Incorrect! Game Over.")
                print(f"The correct sequence was: {''.join(sequence)}")
                print(f"You reached round {round_number}.")
                break
        break

    elif user_choice == '2':
        print("\nPlaying the sound...")
        show_element_options()

    elif user_choice == '3':
        print("\nThank you for your time! See you next time!")
        break
    else:
        print("\nInvalid choice. Please try again.")