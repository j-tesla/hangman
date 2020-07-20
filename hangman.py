import random

print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hint = word[:3] + '-'*(len(word) - 3)

survived_msg = 'You survived!'
hanged_msg = 'You are hanged!'

guess = '-'*len(word)
guessed_letters = []

tries = 8
while tries:
    print('\n' + guess)
    letter = input('Input a letter: ')
    if len(letter) != 1:
        print('You should input a single letter')
    elif not letter.islower():
        print('It is not an ASCII lowercase letter')
    elif letter in guessed_letters:
        print('You already typed this letter')
    elif letter not in word:
        print('No such letter in the word')
        guessed_letters.append(letter)
        tries -= 1
    else:
        for i in range(len(word)):
            if word[i] == letter:
                guess = guess[:i] + letter + guess[i+1:]
        guessed_letters.append(letter)
        if word == guess:
            print('You guessed the word ' + word + '!')
            print(survived_msg)
            break
else:
    print(hanged_msg)
