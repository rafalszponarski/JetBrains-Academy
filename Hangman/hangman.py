from random import choice


def play():
    global won
    global lost

    correct = choice(['python', 'java', 'swift', 'javascript'])
    hidden = ['-'] * len(correct)
    user = []
    attempt = 0

    while True:
        if hidden == list(correct):
            print(f'\nYou guessed the word {correct}!')
            print('You survived!')
            won += 1
            break

        elif attempt == 8:
            print('\nYou lost!')
            lost += 1
            break

        else:
            print('\n' + ''.join(hidden))
            guess = input('Input a letter: ')

            if len(guess) != 1:
                print('Please, input a single letter.')

            elif not guess.islower():
                print('Please, enter a lowercase letter from the English alphabet.')

            elif guess in user:
                print("You've already guessed this letter.")

            elif guess not in correct:
                print("That letter doesn't appear in the word.")
                attempt += 1

            else:
                for index in [i for i, c in enumerate(correct) if c == guess]:
                    hidden[index] = guess

            user.append(guess)


print('H A N G M A N')
won = 0
lost = 0

while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if menu == "play":
        play()

    elif menu == 'results':
        print(f'You won: {won} times.')
        print(f'You lost: {lost} times.')

    elif menu == 'exit':
        break
