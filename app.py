from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from game_logic import Game, Player, generate_random_number, heat
import random
import jsonpickle

app = Flask(__name__)
app.secret_key = "your_secret_key"

Easy = "Easy (Number in the range of 1-5)"
Medium = "Medium (Number in the range of 1-10)"
Hard = "Hard (Number in the range of 1-15)"
 
DIFFICULTIES = {
    1: (Easy, 5, 4),
    2: (Medium, 10, 8),
    3: (Hard, 15, 6)
}

@app.route('/')
def home():
    message = "Enter your name:"
    return render_template('home.html', console_output=message)

@app.route('/exit')
def exit():
    return render_template('exit.html')

@app.route('/win')
def win():
    return render_template('win.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        user_name = request.form['input']
        
        

        game = Game()

        name_result = game.player.set_name(user_name)
        
        if name_result == 3:
            message = "Name cannot be empty."
            return render_template('home.html', console_output=message)
        elif name_result == 2:
            message = "Name can only contain alphabetic characters."
            return render_template('home.html', console_output=message)
        elif name_result == 1:
            message = "Name must be at least 3 characters long."
            return render_template('home.html', console_output=message)

        serialized_game = jsonpickle.encode(game)
        session['current_game'] = serialized_game

        message = f"Welcome {game.player.name}!\n"
        message += "The goal of the game is to guess the correct number.\n"

        message += "What difficulty would you like to play on?\n"
        message += "1 - Easy (1-5)  2 - Medium (1-10)  3 - Hard (1-15)"

        return render_template('playge.html', console_output=message)

@app.route('/playge', methods=['POST'])
def playge():
    if request.method == 'POST':
        serialized_game = session.get('current_game')
        game = jsonpickle.decode(serialized_game)

        diff = request.form['input']
        
        message = "What difficulty would you like to play on?\n"
        message += "1 - Easy (1-5)  2 - Medium (1-10)  3 - Hard (1-15)"

        try:
            diffi = int(diff)
        except ValueError:
            return render_template('playge.html', console_output=message)

        if 1 <= diffi <= 3:
            game.difficulty_string, game.difficulty, game.maxAttempts = DIFFICULTIES[diffi]
            game.targetNumber = random.randint(1, game.difficulty)
            game.attempts = 0  # Reset attempts for each new game

            remaining_attempts = game.maxAttempts - game.attempts

            serialized_game = jsonpickle.encode(game)
            session['current_game'] = serialized_game

            message = game.difficulty_string
            message += f"\nYou have {remaining_attempts} attempts remaining.\n"
            message += "Enter your guess:"

            return render_template('guessge.html', console_output=message)

        return render_template('playge.html', console_output=message)

@app.route('/guessge', methods=['POST'])
def guessge():
    serialized_game = session.get('current_game')
    game = jsonpickle.decode(serialized_game)

    if request.method == 'POST':
        guess = request.form['input']
        
        if guess.isdigit() and 1 <= int(guess) <= game.difficulty:

            guess = int(request.form['input'])

            game.attempts += 1

            if guess == game.targetNumber:
                return render_template('win.html', player_name = game.player.get_name(), attempts=game.attempts, difficulty=game.difficulty_string)

            if game.attempts > (game.maxAttempts - 1):
                return render_template('exit.html', player_name = game.player.get_name(), attempts=game.attempts, difficulty=game.difficulty_string)

        
            remaining_attempts = game.maxAttempts - game.attempts

            message = game.difficulty_string
            message += f"\n{heat(guess, game.targetNumber)}"
            message += f"\nYou have {remaining_attempts} attempts remaining.\n"
            message += "Enter your guess:"

            serialized_game = jsonpickle.encode(game)
            session['current_game'] = serialized_game

            return render_template('guessge.html', console_output=message)
        
        message = game.difficulty_string
        message += "\nInvalid guess, try again."
        message += f"\nYou still have {game.maxAttempts - game.attempts} attempts remaining.\n"
        message += "Enter your guess:"

        serialized_game = jsonpickle.encode(game)
        session['current_game'] = serialized_game

        return render_template('guessge.html', console_output=message)



if __name__ == '__main__':
    app.run(debug=True)
