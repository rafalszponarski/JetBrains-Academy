def is_one_digit(v):
    return True if -10 < v < 10 and v - round(v) == 0 else False


def check(v1, v2, v3):
    msg = ""
    msg += " ... lazy" if is_one_digit(v1) and is_one_digit(v2) else ""
    msg += " ... very lazy" if v1 == 1 or v2 == 1 and v3 == "*" else ""
    msg += " ... very, very lazy" if v1 == 0 or v2 == 0 and v3 in "+-*" else ""
    print("You are" + msg) if msg != "" else ""


memory = 0
while True:
    x, operation, y = input("Enter an equation").split()
    try:
        x = memory if x == 'M' else float(x)
        y = memory if y == 'M' else float(y)

    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    except KeyError:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
    else:

        check(x, y, operation)
        match operation:
            case '+': result = x + y
            case '-': result = x - y
            case '*': result = x * y
            case '/': result = x / y

        print(result)

        if input("Do you want to store the result? (y / n):") == 'y':
            if is_one_digit(result):
                i = 0
                while i <= 2:
                    answer = input(["Are you sure? It is only one digit! (y / n)",
                                    "Don't be silly! It's just one number! Add to the memory? (y / n)",
                                    "Last chance! Do you really want to embarrass yourself? (y / n)"][i])
                    if answer == 'y' and i == 2:
                        i += 1
                        memory = result
                    elif answer == 'y':
                        i += 1
                    elif answer == 'n':
                        break
            else:
                memory = result
        if input("Do you want to continue calculations? (y / n):") == 'n':
            break
