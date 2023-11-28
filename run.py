# Asks the player at the end of the game if he wants to play another game.
def play_again():
    while True:
        user_input = input("Do you fancy another game? (y/n)").lower()
        if user_input == "y" or user_input == "n":
            return user_input == "y"
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


"""
Libraries and imports
"""
while True:
    import dictionary  # Stores random words
    import hangman  # Contains the ascii art for the Hangman
    import random  # Lets us get a random word of the ones stored in dictionary
    from colorama import Fore, Back, Style  # Adds colors
    import time  # Add delay to print out text

    def print_slow(text, speed=0.005):
        for character in text:
            print(character, end="", flush=True)
            time.sleep(speed)
        print()

    # Welcoming ASCii art
    print_slow(f"{Fore.YELLOW}Welcome to: \n")
    print_slow("    __    __     ___    .__   __.  ______ .___  ___.    ___  "
               "   .__   __.")
    print_slow("   |  |  |  |   /   \   |  \ |  | /  ____||   \/   |   /   \ "
               "   |  \ |  |")
    print_slow("   |  |__|  |  /  ^  \  |   \|  ||  |  __ |  \  /  |  /  ^  "
               "\   |   \|  |")
    print_slow("   |   __   | /  /_\  \ |  . `  |   | |_ ||  |\/|  | /  /_\  "
               "\  |  . `  |")
    print_slow("   |  |  |  |/  _____  \|  |\   ||  |__| ||  |  |  |/  _____ "
               " \ |  |\   |")
    print_slow("   |__|  |__|__/     \__|__| \__| \______||__|  |__|__/     "
               f" \__|__| \__|{Style.RESET_ALL}")

    """
    Start function of the game which lets
    the player select to play or to quit the game
    """

    def start_game():
        print()
        print(
            f"{Fore.YELLOW}       ___________________________________________"
            f"___________________{Style.RESET_ALL}")
        print()
        print_slow(f"{Fore.YELLOW}                   You wanna play a game of "
                   f"Hangman?{Style.RESET_ALL}\n")
        print()
        print(
            "Hangman Rules: The computer makes up a word and You try to "
            "guess it. The word to guess is represented by a row of "
            "dashes, one for each letter. You guess a letter by typing "
            "it and press Enter. If the guessed letter is in the word, "
            "the dashes are replaced with the letter. If you guessed "
            "wrong, a part of the hangman is drawn. You continue to "
            "guess until you guessed the whole word or make too many "
            "incorrect guesses. The game ends when the word is guessed"
            "correctly or the hangman is fully drawn.\n")
        print()
        choice = input(f"{Fore.YELLOW}          Please press 'p' to play a"
                       "game or 'q' to leave the game"
                       f"{Style.RESET_ALL}\n").lower()

        if choice == "p":
            while True:
                player_name = input(f"{Fore.YELLOW}              Hi, glad you"
                                    f"chose to play. Please enter your name: "
                                    f"{Style.RESET_ALL}\n")
                # Checks so the player enters a valid name
                if len(player_name) >= 2 and player_name.isalpha():
                    print()
                    print(f"{Fore.BLUE}--------------------------------------"
                          "-------------------------------\n")
                    print(f"Hello {player_name}! Let's start the game, chose a"
                          f"letter..{Style.RESET_ALL}\n")
                    return True
                else:
                    print(f"{Fore.RED}Invalid name. Please enter at least two"
                          f"letters, using only alphabetic characters."
                          f"{Style.RESET_ALL}")
        elif choice == "q":
            print(f"{Fore.BLUE}----------------------------------------------"
                  "----------------------------")
            print()
            print("                                      \|/ ")
            print("                                    ^-O-O-^ ")
            print("----------------------------------ooO--U--Ooo-------------"
                  "-----------------\n")
            print("                Ok, thanks for visiting, have a great day!")
            print()
            print(f"----------------------------------------------------------"
                  f"----------------{Style.RESET_ALL}\n")

        else:
            print("Invalid choice, please enter 'p' start the game or 'q' to"
                  "quit the game \n")
            return start_game()

    """
    Here the game starts and the random word is
    chosen, the player get to chose letter etc
    """
    if start_game():
        answer = random.choice(dictionary.words)
        answer = list(answer)

        game_ove = False

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
                print(f"{Fore.BLUE}___________________________________________"
                      "_____________________________________")
                print("Oops, wrong letter...")
                print(f"\nWrong guesses so far: {Style.RESET_ALL}",
                      guessed_letters_str)
                print()

            # Printing out the picture of hangman if guess is wrong
            print("\n".join(hangman.hangmans[len(guessed_letters)]))

            # Printing out the random word
            print("".join(word))

            # Lets the player chose a letter of choice he thinks is in the word
            guess = input(f"\n{Fore.BLUE}Please, guess a letter: "
                          f"{Style.RESET_ALL}\n")
            print()
            print()

            # Checks for a valid input (only letters and one at a time)
            if len(guess) == 1 and guess.isalpha():
                # Check if the guessed letter has already been guessed
                if guess.lower() in guessed_letters or guess in word:
                    print(f"\n{Fore.RED}You already guessed '{guess.lower()}',"
                          f"try a different letter!{Style.RESET_ALL}\n")
                    # Skip rest of the loop and prompt the user to guess again
                    continue

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

                    guessed_letters_str = " ".join(f"{Fore.YELLOW}{g}"
                                                   f"{Style.RESET_ALL}"
                                                   for g in guessed_letters)

                if guess in word:
                    print(f"\n{Fore.GREEN}Great Guess, keep em coming!"
                          f"{Style.RESET_ALL}\n")

            else:
                print("______________________________________________________"
                      "___________")
                print(f"{Fore.RED}Invalid choice, please enter a letter"
                      f"{Style.RESET_ALL}")

            if not "_ " in word:
                game_over = True
                print(f"{Fore.YELLOW}________________________________________"
                      "___________________________\n")
                print("\nYay, you made it... you guessed the correct word "
                      "which was "
                      + "".join(answer).upper()
                      + " Great job!!")
                print()
                print("               ,,, ")
                print("              (o o) ")
                print(f"----------oOO--( )--OOo----{Style.RESET_ALL}\n")
            elif len(guessed_letters) == len(hangman.hangmans) - 1:
                game_over = True
                print(f"{Fore.RED}___________________________________________"
                      "_____________________\n")
                print("\nSorry, you lost... The word was: "
                      + "".join(answer).upper())
                print()
                print("       \|||/ ")
                print("       (o o) ")
                print(f"----ooO-(_)-Ooo----{Style.RESET_ALL}\n")

        # Ask if the player wants to play again
        if not play_again():
            print()
            print()
            print(f"{Fore.BLUE}_____________________________________________"
                  "______________________________\n")
            print("                   Thank you for playing, see you soon "
                  "again!!!\n")
            print()
            print("                                     \|/ ")
            print("                                   ^-O-O-^ ")
            print("                            -----ooO--U--Ooo-----\n")
            print()
            print()
            print(f"________________________________________________________"
                  f"______________________{Style.RESET_ALL}")
            break  # Exit the loop if they player chose to end
