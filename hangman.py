import random

print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

survived_msg = 'You survived!'
hanged_msg = 'You are hanged!'

guess = input('Guess the word: ')

if guess == word:
    print(survived_msg)
else:
    print(hanged_msg)
