

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
    print_slow(f"{Fore.YELLOW}Welcome to: \n")
    print_slow("    __    __     ___    .__   __.  ______ .___  ___.    ___    .__   __.")
    print_slow("   |  |  |  |   /   \   |  \ |  | /  ____||   \/   |   /   \   |  \ |  |") 
    print_slow("   |  |__|  |  /  ^  \  |   \|  ||  |  __ |  \  /  |  /  ^  \  |   \|  |")
    print_slow("   |   __   | /  /_\  \ |  . `  |   | |_ ||  |\/|  | /  /_\  \ |  . `  |")
    print_slow("   |  |  |  |/  _____  \|  |\   ||  |__| ||  |  |  |/  _____  \|  |\   |")
    print_slow(f"   |__|  |__|__/     \__|__| \__| \______||__|  |__|__/     \__|__| \__|{Style.RESET_ALL}")

    """
    Start function of the game which lets the player select to play or to quit the game
    """
    def start_game():
        print()
        print(f"{Fore.YELLOW}       ______________________________________________________________{Style.RESET_ALL}")
        print()
        print_slow(f"{Fore.YELLOW}                   You wanna play a game of Hangman?{Style.RESET_ALL}\n")
        choice = input(f"{Fore.YELLOW}          Please press 'p' to play a game or 'q' to leave the game{Style.RESET_ALL}\n").lower()

        print("Hangman Rules: The computer makes up a word and You try to guess it.  The word to guess is represented by a row of dashes, one for each letter.  You guess a letter by typing it and press Enter.  If the guessed letter is in the word, the dashes are replaced with the letter.  If you guessed wrong, a part of the hangman is drawn.  You continue to guess until you guessed the whole word or make too many incorrect guesses.  The game ends when the word is guessed correctly or the hangman is fully drawn.")
        if choice == 'p':
            while True:
                player_name = input(f"{Fore.YELLOW}              Hi, glad you chose to play. Please enter your name: {Style.RESET_ALL}\n")
                # Checks so the player enters a valid name
                if len(player_name) >= 2 and player_name.isalpha():
                    print()
                    print("---------------------------------------------------------------------\n")
                    print(f"{Fore.BLUE}Hello {player_name}! Let's start the game, chose a letter...{Style.RESET_ALL}\n")
                    return True
                else:
                    print(f"{Fore.RED}Invalid name. Please enter at least two letters, using only alphabetic characters.{Style.RESET_ALL}")
        elif choice == 'q':
            print()
            print(f"{Fore.BLUE}                      \|/ ")
            print("                    ^-O-O-^ ")    
            print("------------------ooO--U--Ooo-----\n")
            print(f"Ok, thanks for visiting, have a great day!{Style.RESET_ALL}")           
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
                print()
                print("\nYOU HAVE GUESSED THESE LETTERS SO FAR WICH ARE NOT IN THE WORD: ", guessed_letters_str)
                print()


            # Printing out the picture of hangman if guess is wrong
            print("\n".join(hangman.hangmans[len(guessed_letters)]))

            # Printing out the random word
            print("".join(word))


            # Lets the player chose a letter of choice he thinks is in the word
            guess = input(f"\n{Fore.GREEN}Please, guess a letter: {Style.RESET_ALL}\n")

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
                    guessed_letters.append(guess.lower())

                    guessed_letters_str = ' '.join(f"{Fore.RED}{g}{Style.RESET_ALL}" for g in guessed_letters)

            else:
                print("_________________________________________________________________")
                print(f"{Fore.RED}Invalid choice, please enter a letter{Style.RESET_ALL}")

            if not "_ " in word:
                game_over = True
                print("_________________________________________________________________\n")
                print("\nYay, you made it... you guessed the correct word which was "  + "".join(answer).upper() + " Great job!!")
                print()
                print("               ,,, ")
                print("              (o o) ")
                print("----------oOO--( )--OOo----\n")
            elif len(guessed_letters) == len(hangman.hangmans) -1:
                game_over = True
                print("________________________________________________________________\n")
                print("\nSorry, you lost... The word was: " + "".join(answer).upper())
                print()
                print("       \|||/ ")
                print("       (o o) ")
                print("----ooO-(_)-Ooo----\n")

        # Ask if the player wants to play again
        if not play_again():
            print("____________________________________________________________________\n")
            print("Thank you for playing, see you soon again!!!\n")
            print()
            print("                      \|/ ")
            print("                    ^-O-O-^ ")    
            print("------------------ooO--U--Ooo-----\n")
            break # Exit the loop if they player chose to end 
