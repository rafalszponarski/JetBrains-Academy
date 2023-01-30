def calculator(formula, memory):
    if '=' in formula:
        key, value = formula.replace(' ', '').split('=')

        if not key.isalpha():
            print("Invalid identifier")

        elif value.isnumeric():
            memory[key] = float(value)
        elif value in memory.keys():
            memory[key] = float(memory[value])
        else:
            print("Invalid assignment")

    elif any(k in formula for k in '+-*/^'):
        for k, v in memory.items():
            formula.replace(k, str(v))

        print(round(eval(formula, {"builtins": None}, memory)))

    elif formula.strip() in memory.keys():
        print(round(memory[formula.strip()]))

    else:
        print("Unknown variable")


def menu():
    memory = {}
    while True:
        user = input()

        if user == '/exit':
            print("Bye!")
            break

        elif user == '/help':
            print('Super helpful help message!')

        elif user.startswith('/'):
            print('Unknown command')

        elif not (user.count('(') == user.count(')') and not any(k*2 in user for k in '+-*/^=') and user.count('=') <= 1):
            print('Invalid expression')

        elif user:
            calculator(user, memory)


if __name__ == '__main__':
    menu()
