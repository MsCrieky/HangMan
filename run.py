

import dictionary # Stores random words
import hangman # Contains the ascii art for the Hangman
import random # Lets us get a random word of the ones stored in dictionary
from rich import print # Lets us choose different colors for our letters

# Welcoming ASCii art
print("Welcome to: \n")
print()
print("[bold green] __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.[/bold green]")
print("[bold green]|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |[/bold green]")
print("[bold green]|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |[/bold green]") 
print("[bold green]|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |[/bold green]") 
print("[bold green]|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |[/bold green]") 
print("[bold green]|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|[/bold green]")
print("[bold green]===============================================================================[/bold green]\n")

print(" ___________.._______ ")
print("| .__________))______| ")
print(" | | / /      || ")
print(" | |/ /       || ")
print(" | | /        ||.-''. ")
print(" | |/         |/  _  \ ")
print(" | |          ||  `/,| ")
print(" | |          (\\`_.' ")
print(" | |         .-`--'. ")
print(" | |        /Y . .Y\ ")
print(" | |       // |   |\\ ")
print(" | |      //  | . | \\ ")
print(" | |     ')   |   |  (` ")
print(" | |          ||'|| ")
print(" | |          || || ")
print(" | |          || || ")
print(" | |          || || ")
print(" | |         /     \ ")
print(" ====================== \n")

def start_game():
    print("You wanna play a game of Hangman?\n")
    choice = input("Please press 'p' to play a game or 'q' to leave the game\n").lower()
    if choice == 'p':
        player_name = input("Hi, glad you chose to play. Please enter your name: \n")
        print()
        print(f"Hello {player_name}! Let's start the game, chose a letter...\n")
        return True
    elif choice == 'q':
        print("Ok, thanks for visiting, have a great day!")
        return False
    else:
        print("Invalid choice, please enter 'p' start the game or 'q' to quit the game \n")
        return start_game()



