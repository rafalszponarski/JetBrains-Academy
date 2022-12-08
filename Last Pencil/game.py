pencils = 0
while True:
    try:
        pencils = int(input('How many pencils would you like to use: '))
    except ValueError:
        print("The number of pencils should be numeric")
        continue

    if pencils < 1:
        print("The number of pencils should be positive")
        continue

    break

name = ''
while True:
    if name not in ['Jack', 'John']:
        name = input(f'Who will be the first (John, Jack): ')

    match name:
        case 'Jack':
            print(f"{'|' * pencils}\nJack's turn: ")

            if pencils % 4 == 0:
                print('3')
                pencils -= 3
            elif pencils % 4 == 3:
                print('2')
                pencils -= 2
            else:
                print('1')
                pencils -= 1

            if pencils == 0:
                print('John won!')
                break
            else:
                name = 'John'
                continue

        case 'John':
            print('|' * pencils)

            take = input("John's turn! ")
            if take not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                name = 'John'
                continue

            elif int(take) > pencils:
                print('Too many pencils were taken.')
                name = 'John'
                continue

            pencils -= int(take)

            if pencils == 0:
                print('Jack won!')
                break
            else:
                name = 'Jack'
                continue

        case _:
            print(f'Choose between John and Jack')
            continue
