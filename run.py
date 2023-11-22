# Asks the player at the end of the game if he wants to play another game.
def play_again():
    return input("Do you fancy another game? (y/n)").lower() == 'y'

while True:
    import dictionary  # Stores random words
    import hangman  # Contains the ascii art for the Hangman
    import random  # Lets us get a random word of the ones stored in dictionary

    # Welcoming ASCii art
    print("Welcome to: \n")
    print(" __    __     ___    .__   __.  ______ .___  ___.    ___    .__   __.")
    print("|  |  |  |   /   \   |  \ |  | /  ____||   \/   |   /   \   |  \ |  |")
    print("|  |__|  |  /  ^  \  |   \|  ||  |  __ |  \  /  |  /  ^  \  |   \|  |")
    print("|   __   | /  /_\  \ |  . `  |   | |_ ||  |\/|  | /  /_\  \ |  . `  |")
    print("|  |  |  |/  _____  \|  |\   ||  |__| ||  |  |  |/  _____  \|  |\   |")
    print("|__|  |__|__/     \__|__| \__| \______||__|  |__|__/     \__|__| \__|")

    """
    Start function of the game which lets the player select to play or to quit the game
    """
    def start_game():
        print("You wanna play a game of Hangman?\n")
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
                word.append("_")

        guessed_letters = []

        # Print out made guesses
        while not game_over:
            if len(guessed_letters) > 0:
                print("--------------------------------------------------\n")
                print("\nYou have guessed these letter so far: " + " ".join(guessed_letters))
                print("--------------------------------------------------\n")
                print()

            # Printing out the picture of hangman if guess is wrong
            print("\n".join(hangman.hangmans[len(guessed_letters)]))

            # Printing out the random word
            print("".join(word))

            # Lets the player chose a letter of choice he thinks is in the word
            guess = input("\nPlease, guess a letter: ")

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
                guessed_letters.append(guess)

            if not "_" in word:
                game_over = True
                print("-----------------------------------\n")
                print("\nYay, you made it.... Great job!!")
                print("         ,,, ")
                print("        (o o) ")
                print("----oOO--( )--OOo---- ")
            elif len(guessed_letters) == len(hangman.hangmans) -1:
                game_over = True
                print("-------------------------------------------------\n")
                print("\nSorry, you lost... The word was: " + "".join(answer))
                print("       \|||/ ")
                print("       (o o) ")
                print("----ooO-(_)-Ooo---- ")

        # Ask if the player wants to play again
        if not play_again():
            print("-------------------------------------------------\n")
            print("Thank you for playing, see you soon again!!!\n")
            print()
            print("                      \|/ ")
            print("                    ^-O-O-^ ")    
            print("------------------ooO--U--Ooo-----")
            break # Exit the loop if they player chose to end 


