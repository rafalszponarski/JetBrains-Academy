from random import randint


mark = 0
levels = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}
print(f"Which level do you want? Enter a number:")
level = int(input('\n'.join(levels.values()) + '\n'))

while level not in [1, 2]:
    print("Incorrect format.")
    print(f"Which level do you want? Enter a number:")
    level = int(input('\n'.join(levels.values()) + '\n'))


for _ in range(5):
    if level == 1:
        task = f"{randint(2, 9)} {['+', '-', '*'][randint(0, 2)]} {randint(2, 9)}"
        correct = eval(task)

    elif level == 2:
        task = randint(11, 29)
        correct = task ** 2

    print(task)

    while True:
        try:
            user = int(input())

            if user == correct:
                print("Right!")
                mark += 1
            else:
                print("Wrong!")

            break

        except ValueError:
            print("Incorrect format.")


save = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")

if save.lower() in ['y', 'yes']:
    name = input("What is your name?\n")

    with open("results.txt", "a") as f:
        f.write(f"{name}: {mark}/5 in level {level} ({levels[level]})")

    print('The results are saved in "results.txt".')
