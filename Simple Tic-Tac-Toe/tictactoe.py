def board():
    print('-' * 9)
    for i in game:
        print(f"| {' '.join(i)} |")
    print('-' * 9)


game = [['_' for i in range(3)] for j in range(3)]
board()

wait = 'X'
play = 'O'
win = set()

while True:
    play, wait = wait, play
    coords = input()

    if len([x for x in coords.split() if x.isdigit()]) != 2:
        print("You should enter numbers!")
    else:
        row, col = [int(x) for x in coords.split()]

        if row > 3 or col > 3:
            print("Coordinates should be from 1 to 3!")

        elif game[row - 1][col - 1] == "_":
            game[row - 1][col - 1] = play
            board()

            if not win:
                for i in range(3):
                    if game[i][0] == game[i][1] == game[i][2] and game[i][0] != '_':
                        win.add(game[i][0])
                    elif game[0][i] == game[1][i] == game[2][i] and game[0][i] != '_':
                        win.add(game[0][i])
                    elif (game[0][0] == game[1][1] == game[2][2]
                          or game[0][2] == game[1][1] == game[2][0])\
                            and game[1][1] != '_':
                        win.add(game[1][1])

            if not win and '_' not in [x for sublist in game for x in sublist]:
                print("Draw")
                break

            if win:
                print(f"{list(win)[0]} wins")
                break

            continue

        else:
            print("This cell is occupied! Choose another one!")
