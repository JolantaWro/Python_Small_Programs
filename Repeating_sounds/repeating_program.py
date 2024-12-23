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


SOUND_MAP = {
    'A': 'soundA.wav',
    'S': 'soundS.wav',
    'D': 'soundD.wav',
    'F': 'soundF.wav'
}

def show_element_options():
    """Displays the sound options to the player."""
    for key, sound in SOUND_MAP.items():
        print(f"\nWhen you hear this sound:")
        playsound(sound)
        time.sleep(1)
        print(f"Press '{key}'.")

def play_sequence(sequence):
    """Plays the sequence of sounds"""
    for element in sequence:
        playsound(SOUND_MAP[element])
        time.sleep(0.5)

def get_new_element():
    """Generates a new random element from the valid keys."""
    return choice(list(SOUND_MAP.keys()))

def play_round():
    """Runs the main game loop for a round."""
    sequence = []
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        new_element = get_new_element()
        sequence.append(new_element)

        play_sequence(sequence)
        player_input = input("Repeat the sequence: ").strip().upper()

        if player_input == ''.join(sequence):
            print("Correct! Get ready for the next round!")
            round_number += 1
            time.sleep(2)
        else:
            print("Incorrect! Game Over.")
            print(f"The correct sequence was: {''.join(sequence)}")
            print(f"You reached round {round_number}.")
            break

def main():
    """Main function to control the game flow."""
    print("\n=== Welcome to the Sound Repetition Game! ===")

    while True:
        print("\nAre you ready for the game?")
        print("1. Yes, I am ready!")
        print("2. I want to listen to the sound options.")
        print("3. Exit the game.")

        user_choice = input("Choose an option (1, 2, 3): ").strip()

        if user_choice == '1':
            print("\nGreat! Let's start the game!")
            play_round()
            break

        elif user_choice == '2':
            print("\nPlaying the sound options...")
            show_element_options()

        elif user_choice == '3':
            print("\nThank you for playing! See you next time!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()