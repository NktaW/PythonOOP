#import module
import random
#create lives variable
lives = 9
#make list of words
words = ['pizza', 'pasta', 'spoon', 'space', 'green', 'beard']
#create variable that choose random word from the list
secret_word = random.choice(words)
#create clue variable
clue = list('??????')
#create heart sybol to show user how many lives left
heart_symbol = u'\u2764'
#create variable, wich contains info if user guessed word correctly
guessed_word_correctly = False

#create while loop that checks if letter exist in the guessing word.
def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives remaining' + heart_symbol * lives)
    guess = input('Guess word, or letter of the word:  ')

    #if guessed word is correct the loop breaks
    if guess == secret_word:
        guessed_word_correctly = True
        break
    #if letter exist in guessed word, clue updates
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    #if answer incorrect, will lost 1 live
    else:
        print('Incorrect! you lost one live')
        lives = lives - 1

if guessed_word_correctly:
    print('Congraz, you won!  Secret word was:  ' + secret_word)
else :
    print('You lost! The secret word was:  ' + secret_word)