from sqlite3 import connect
from random import randint


with connect('card.s3db') as database:
    bank = database.cursor()
    bank.execute('DROP TABLE IF EXISTS card;')
    bank.execute('''
                CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0);
                ''')


def card_generate():
    new = '400000' + ''.join([str(randint(0, 9)) for _ in range(9)])
    luhn = 0

    for i in range(len(new)):
        if i % 2 == 0:
            luhn += int(new[i]) * 2 if int(new[i]) * 2 < 10 else int(new[i]) * 2 - 9

        if i % 2 != 0:
            luhn += int(new[i])

    return new + str((10 - (luhn % 10)) % 10)


def card_check(card_number):
    digits = list(map(int, card_number))
    check_sum = sum(digits[-1::-2] + [sum(divmod(2 * d, 10)) for d in digits[-2::-2]])

    return check_sum % 10 == 0


while True:
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    user = input()

    match user:

        case '1':
            card = card_generate()
            pin = randint(1000, 9999)

            bank.execute(f'INSERT INTO card(number, pin) VALUES({card}, {pin})')
            database.commit()

            print('Your card has been created')
            print(f'Your card number:\n{card}')
            print(f'Your card PIN:\n{pin}')

        case '2':
            card = input('Enter your card number: ')
            pin = input('Enter your PIN: ')

            login = bank.execute(f'SELECT 1 FROM card WHERE number = {card} AND pin = {pin} LIMIT 1').fetchone()

            if login:
                print('You have successfully logged in!')

                while True:
                    print('1. Balance')
                    print('2. Add income')
                    print('3. Do transfer')
                    print('4. Close account')
                    print('5. Log out')
                    print('0. Exit')
                    account = input()

                    match account:

                        case '1':
                            balance = bank.execute(f'SELECT balance FROM card WHERE number = {card}').fetchone()[0]
                            print(f'Balance: {balance}')

                        case '2':
                            income = int(input('Enter income: '))

                            balance = bank.execute(f'SELECT balance FROM card WHERE number = {card}').fetchone()[0]
                            bank.execute(f'UPDATE card SET balance = {balance + income} WHERE number = {card}')
                            database.commit()

                            print('Income was added!')

                        case '3':
                            t_card = input('Enter card number:')

                            if card_check(t_card):

                                if bank.execute(f'SELECT 1 FROM card WHERE number = {t_card} LIMIT 1;').fetchone():
                                    t_amount = int(input('Enter how much money you want to transfer:'))
                                    balance = bank.execute(f'SELECT balance FROM card WHERE number = {card}').fetchone()[0]

                                    if balance >= t_amount:
                                        t_balance = bank.execute(f'SELECT balance FROM card WHERE number = {t_card}').fetchone()[0]
                                        bank.execute(f'UPDATE card SET balance = {balance - t_amount} WHERE number = {card}')
                                        bank.execute(f'UPDATE card SET balance = {t_balance + t_amount} WHERE number = {t_card}')
                                        database.commit()
                                        print('Success!')

                                    else:
                                        print('Not enough money!')

                                else:
                                    print('Such a card does not exist.')

                            else:
                                print('Probably you made a mistake in the card number. Please try again!')

                        case '4':
                            bank.execute(f'DELETE FROM card WHERE number = {card}')
                            database.commit()

                            print('The account has been closed!')
                            break

                        case '5':
                            print('You have successfully logged out!')
                            break

                        case '0':
                            print('Bye!')
                            exit()

            else:
                print('Wrong card number or PIN!')

        case '0':
            print('Bye!')
            exit()
