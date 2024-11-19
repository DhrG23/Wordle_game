from flask import Flask, request, render_template, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Define the correct word
CORRECT_WORD = "flask"

@app.route('/', methods=['GET', 'POST'])
def wordle():
    if 'game_state' not in session:
        # Initialize session variables
        session['game_state'] = {
            'attempts': [],
            'keyboard': {chr(c): None for c in range(97, 123)},  # a-z with initial state None
            'game_over': False,
            'message': ""
        }

    game_state = session['game_state']

    if request.method == 'POST' and not game_state['game_over']:
        user_word = request.form['word'].lower()

        if len(user_word) != len(CORRECT_WORD):
            game_state['message'] = f"Word must be {len(CORRECT_WORD)} letters long."
        elif len(game_state['attempts']) >= 5:
            game_state['message'] = f"Game over! The correct word was '{CORRECT_WORD}'."
            game_state['game_over'] = True
        else:
            feedback = []
            for i, char in enumerate(user_word):
                if char == CORRECT_WORD[i]:
                    feedback.append('green')  # Correct position
                    game_state['keyboard'][char] = 'green'
                elif char in CORRECT_WORD:
                    feedback.append('yellow')  # Correct letter, wrong position
                    if game_state['keyboard'][char] != 'green':  # Avoid downgrading green
                        game_state['keyboard'][char] = 'yellow'
                else:
                    feedback.append('gray')  # Incorrect letter
                    game_state['keyboard'][char] = 'gray'

            game_state['attempts'].append({'word': user_word, 'feedback': feedback})

            if user_word == CORRECT_WORD:
                game_state['message'] = "Correct! You guessed the word!"
                game_state['game_over'] = True
            elif len(game_state['attempts']) >= 5:
                game_state['message'] = f"Game over! The correct word was '{CORRECT_WORD}'."
                game_state['game_over'] = True
            else:
                game_state['message'] = f"Wrong! Attempts left: {5 - len(game_state['attempts'])}"

        session.modified = True

    return render_template('wordle.html', game_state=game_state)

@app.route('/reset')
def reset():
    session.pop('game_state', None)
    return redirect(url_for('wordle'))

if __name__ == '__main__':
    app.run(debug=True)
