from random import choice


win = {
    'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
    'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning']
}

score = {}
with open("rating.txt") as read:
    for line in read:
        n, s = line.split()
        score[n] = int(s)

name = input("Enter your name:")
print(f"Hello, {name}")

if name not in score.keys():
    score[name] = 0

game = input()
game = ['rock', 'paper', 'scissors'] if game == '' else game.split(',')
print("Okay, let's start")

while True:
    user = input()
    computer = choice(list(game))

    if user == '!exit':
        print("Bye!")
        exit()

    elif user == '!rating':
        print(f"Your rating: {score[name]}")

    elif user not in game:
        print("Invalid input")

    elif user == computer:
        score[name] += 50
        print(f"There is a draw ({user})")

    elif computer in win[user]:
        score[name] += 100
        print(f"Well done. The computer chose {computer} and failed")

    else:
        print(f"Sorry, but the computer chose {computer}")
