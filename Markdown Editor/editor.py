def header(t):
    while True:
        level = int(input('Level:'))

        if level in range(1, 6):
            break
        else:
            print('The level should be within the range of 1 to 6')

    return t + f"{level*'#'} {input('Text:')}\n"


def lists(t, option):
    while True:
        rows = int(input('Number of rows:'))

        if rows > 1:
            break
        else:
            print('The number of rows should be greater than zero')

    data = [input(f'Row #{i + 1}') for i in range(rows)]

    match option:
        case 'ordered-list':
            result = map(lambda x, y: f"{y}. {x}\n", data, range(1, rows + 1))

        case 'unordered_list':
            result = map(lambda x: f"* {x}\n", data)

    return t + ''.join(result)


functions = {
    "plain": lambda x: x + input('Text:'),
    "bold": lambda x: x + f'**{input("Text:")}**',
    "italic": lambda x: x + f'*{input("Text:")}*',
    "link": lambda x: x + f'[{input("Label:")}]({input("URL:")})',
    "inline-code": lambda x: x + f'`{input("Text:")}`',
    "new-line": lambda x: x + '\n',
    "header": header,
    "ordered-list": lists,
    "unordered-list": lists,
}


txt = ''
while True:
    user = input('Choose a formatter: ')
    if user == '!done':
        with open("output.md", "w") as f:
            f.writelines(txt)
        break

    elif user == '!help':
        print(f"Available formatters: {' '.join(functions.keys())}\nSpecial commands: !help !done")

    elif user not in functions:
        print("Unknown formatter or command. Please try again.")

    elif 'ordered-list' in user:
        answer = functions[user](txt, user)
        print(answer)
        txt = answer

    else:
        answer = functions[user](txt)
        print(answer)
        txt = answer
