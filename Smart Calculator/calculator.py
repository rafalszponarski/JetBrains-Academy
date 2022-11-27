import re

user_vars = dict()
while True:
    user_input = input().replace(" ", "")
    if user_input == "/exit":
        print("Bye!")
        break
    elif user_input == "/help":
        print("The program calculates the expression")
    elif user_input.startswith("/"):
        print("Unknown command")
    elif not user_input:
        continue
    elif "=" in user_input:
        if not user_input.split("=")[0].isalpha():
            print("Invalid identifier")
        elif user_input.count("=") > 1 \
                or not user_input.split("=")[1].isnumeric() \
                and user_input.split("=")[1] not in user_vars:
            print("Invalid assignment")
        else:
            user_vars[user_input.split("=")[0]] = user_input.split("=")[1]

    else:
        expr_vars = filter(lambda a: a.isalpha(), re.split("[+\-*/%()]", user_input))
        for var in expr_vars:
            if var in user_vars:
                val = user_vars[var]
                while not str(val).isnumeric():
                    val = user_vars[val]
                user_input = user_input.replace(var, val)
            else:
                print("Unknown variable")
                break
        else:
            if "//" in user_input:
                print("Invalid expression")
            else:
                try:
                    result = eval(user_input)
                    print(int(result) if int(result) == result else result)
                except Exception:
                    print("Invalid expression")

# This solution belongs to Bartosz Sójka and is much better, that's why I will put them instead of mine
# His profile is available here: https://hyperskill.org/profile/37611696