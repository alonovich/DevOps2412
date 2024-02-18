def welcome():
    name = input("Hi, What is your name?\n")
    print("Hello", name, "and wellcome to the World Of Games.\n"
                         "Here you can find many cool games to play.")
    print()


welcome()


def load_game():
    while True:
        user_input = input("Please choose a game from the list to play: \n"
                           "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                           "back. \n"
                           "2. Guess Game - guess a number and see if you chose like the computer. \n"
                           "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")
        if user_input == "1":
            diff_menu = ("1", "2", "3", "4", "5")
            while True:
                print()
                user_diff = input("Welcome to Memory Game. Please choose a game difficulty between 1-5:\n")
                if user_diff in diff_menu:
                    print("lets play Memory Game. Game difficulty is", user_diff)
                    exit()
                else:
                    print("Not valid game difficulty. Please choose a number between 1-5")
                    continue
        elif user_input == "2":
            diff_menu = ("1", "2", "3", "4", "5")
            while True:
                print()
                user_diff = input("Welcome to Guess Game. Please choose a game difficulty between 1-5: \n")
                if user_diff in diff_menu:
                    print("Lets play Guess Game. Game difficulty is", user_diff)
                    exit()
                else:
                    print("Not valid game difficulty. Please choose a number between 1-5")
                    continue
        elif user_input == "3":
            diff_menu = ("1", "2", "3", "4", "5")
            while True:
                print()
                user_diff = input("Welcome to Currency Roulette. Please choose a game difficulty between 1-5:\n")
                if user_diff in diff_menu:
                    print("Lets play Currency Roulette. Game difficulty is", user_diff)
                    exit()
                else:
                    print("Not valid game difficulty. Please choose a number between 1-5")
                    continue
        else:
            print("Not available. Please Choose a number between 1-3")
            print()
            continue


load_game()
