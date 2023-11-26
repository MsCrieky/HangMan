

# Asks the player at the end of the game if he wants to play another game.
def play_again():
    return input("Do you fancy another game? (y/n)").lower() == 'y'

"""
Libraries and imports
"""
while True:
    import dictionary  # Stores random words
    import hangman  # Contains the ascii art for the Hangman
    import random  # Lets us get a random word of the ones stored in dictionary
    from colorama import Fore, Back, Style # Adds colors
    import time # Add delay to print out text

    def print_slow(text, speed = 0.005):
        for character in text:
            print(character, end ='', flush = True)
            time.sleep(speed)
        print()

    # Welcoming ASCii art
    print_slow("Welcome to: \n")
    print_slow(" __    __     ___    .__   __.  ______ .___  ___.    ___    .__   __.")
    print_slow("|  |  |  |   /   \   |  \ |  | /  ____||   \/   |   /   \   |  \ |  |") 
    print_slow("|  |__|  |  /  ^  \  |   \|  ||  |  __ |  \  /  |  /  ^  \  |   \|  |")
    print_slow("|   __   | /  /_\  \ |  . `  |   | |_ ||  |\/|  | /  /_\  \ |  . `  |")
    print_slow("|  |  |  |/  _____  \|  |\   ||  |__| ||  |  |  |/  _____  \|  |\   |")
    print_slow("|__|  |__|__/     \__|__| \__| \______||__|  |__|__/     \__|__| \__|")

    """
    Start function of the game which lets the player select to play or to quit the game
    """
    def start_game():
        print()
        print("______________________________________________________________")
        print()
        print_slow("You wanna play a game of Hangman?\n")
        choice = input("Please press 'p' to play a game or 'q' to leave the game\n").lower()
        if choice == 'p':
            player_name = input("Hi, glad you chose to play. Please enter your name: \n")
            print()
            print("-------------------------------------------------------------\n")
            print(f"Hello {player_name}! Let's start the game, chose a letter...\n")
            return True
        elif choice == 'q':
            print("Ok, thanks for visiting, have a great day!")
            return False
        else:
            print("Invalid choice, please enter 'p' start the game or 'q' to quit the game \n")
            return start_game()

    """
    Here the game starts and the random word is chosen, the player get to chose letter etc
    """
    if start_game():
        answer = random.choice(dictionary.words)
        answer = list(answer)

        game_over = False

        # Creates an empty word
        word = []
        for i in range(0, len(answer)):
            if answer[i] == " ":
                word.append(" ")
            else:
                word.append("_ ")

        guessed_letters = []

        # Print out made guesses
        while not game_over:
            if len(guessed_letters) > 0:
                print("-----------------------------------------------------------------------------------------\n")
                print("\nYOU HAVE GUESSED THESE LETTERS SO FAR WICH ARE NOT IN THE WORD: ", guessed_letters_str)
                print("----------------------------------------------------------------------------------------\n")
                print()

            # Printing out the picture of hangman if guess is wrong
            print("\n".join(hangman.hangmans[len(guessed_letters)]))

            # Printing out the random word
            print("".join(word))

            # Lets the player chose a letter of choice he thinks is in the word
            guess = input("\nPlease, guess a letter: \n")

            # Checks for a valid input (only letters and one at a time)
            if len(guess) == 1 and guess.isalpha():

                # Keep the wrong guesses
                wrong_guesses = True

                """ 
                Checks if the guessed letter is in the random word
                """
                i = 0
                for letter in answer:
                    if letter == guess:
                        word[i] = letter
                        wrong_guesses = False
                    i += 1

                # Put wrong guesses in a list
                if wrong_guesses:
                    guessed_letters.append(guess.upper())

                    guessed_letters_str = ' '.join(f"{Fore.RED}{g}{Style.RESET_ALL}" for g in guessed_letters)

            else:
                print("Invalid choice, please enter a letter")

            if not "_ " in word:
                game_over = True
                print("________________________________________\n")
                print("\nYay, you made it.... you guessed the correct word which was "  + "".join(answer).upper() + " Great job!!")
                print()
                print("         ,,, ")
                print("        (o o) ")
                print("----oOO--( )--OOo----\n")
            elif len(guessed_letters) == len(hangman.hangmans) -1:
                game_over = True
                print("____________________________________________________\n")
                print("\nSorry, you lost... The word was: " + "".join(answer).upper())
                print()
                print("       \|||/ ")
                print("       (o o) ")
                print("----ooO-(_)-Ooo----\n")

        # Ask if the player wants to play again
        if not play_again():
            print("__________________________________________________\n")
            print("Thank you for playing, see you soon again!!!\n")
            print()
            print("                      \|/ ")
            print("                    ^-O-O-^ ")    
            print("------------------ooO--U--Ooo-----\n")
            break # Exit the loop if they player chose to end 
