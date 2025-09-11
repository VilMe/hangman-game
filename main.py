from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana'])

    username: str = input('What is your name? >>')
    print(f'Welcome to hangman, {username}')


    #Setup
    guessed: str = '' # keep track of what letters were guessed
    tries: int = 3 #how many incorrect guesses are allowed 

    while tries > 0:
        blanks: int = 0

        print('Word', end='')
        for char in word: