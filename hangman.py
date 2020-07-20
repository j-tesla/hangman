import random

print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hint = word[:3] + '-'*(len(word) - 3)

survived_msg = 'You survived!'
hanged_msg = 'You are hanged!'

guess = '-'*len(word)

tries = 8
while tries:
    print('\n' + guess)
    letter = input('Input a letter: ')
    if letter not in word:
        print('No such letter in the word')
        tries -= 1
    elif letter in guess:
        print('No improvements')
        tries -= 1
    else:
        for i in range(len(word)):
            if word[i] == letter:
                guess = guess[:i] + letter + guess[i+1:]
        if word == guess:
            print(guess + '\n' + 'You guessed the word!')
            print(survived_msg)
            break
if tries == 0:
    print(hanged_msg)


# if guess == word:
#     print(survived_msg)
# else:
#     print(hanged_msg)
