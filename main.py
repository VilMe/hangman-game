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

        print('Word ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks+=1
    
        print() # adds a blank line

        guess: str = input('Enter a letter: ')


        if blanks == 0 or guess == word:
            print('You got it!')
            break
        


        # if guess == word:
        #     blanks = 0 
        #     print('made into guesssed conditional')
        #     print('You got it!')
        #     return blanks

        if len(guess) > 1:
            print("Please enter a single letter to continue")
            continue

        if guess in guessed:
            print(f'You already used: "{guess}". Please try another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong...({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining... You lose.')
                break


if __name__ == '__main__':
    run_game()