print("Hello! My name is Aid.")
print("I was created in 2022.")

print("Please, remind me your name.")
print(f"What a great name you have, {input('Please, remind me your name.')}!")

print('Let me guess your age.')
print("Enter remainders of dividing your age by 3, 5 and 7.")
rem3 = int(input("Enter remainders of dividing your age by 3: "))
rem5 = int(input("Enter remainders of dividing your age by 5: "))
rem7 = int(input("Enter remainders of dividing your age by 7: "))
print(f"Your age is {(rem3 * 70 + rem5 * 21 + rem7 * 15) % 105}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
num = int(input())
for i in range(num+1): print(f"{i}!")

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
while True:
    if input() == '2': print("Congratulations, have a nice day!"); break
    else: print("Please, try again.")

print('Congratulations, have a nice day!')
