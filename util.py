def greet(game):
    name = input("Please enter your name: ")
    while name_validate(game, name) != 0:
        name = input("Please enter a valid name: ")
    clear()
    print(f"Welcome {game.player.name}!")
    print("The goal of the game is to guess the correct number.\n")

def name_validate(game, name):
    # Your existing name validation logic here
    pass

def clear():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def check_user_guess(game, user_guess):
    # Your existing check_user_guess function code here
    pass
