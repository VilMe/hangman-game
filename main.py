from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana', 'Goose', 'lovingly', 'manageable'])

    username: str = input('What is your name? >>')
    print(f'Welcome to hangman, {username}')


    #Setup
    guessed: str = '' # keep track of what letters were guessed
    tries: int = 3 #how many incorrect guesses are allowed 

    while tries > 0:
        blanks: int = 0

        print('Word', end='')
        for char in word:
            if char in word:
                print(char, end='')
            else:
                print('_', end='')
                blanks+=1
    
        print() # adds a blank line


        if blanks == 0:
            print('You got it!')
            break
        
        guess: str = input('Enter a letter: ')

        if guess in guessed:
            print(f'You already used: "{guess}". Please try another letter!')