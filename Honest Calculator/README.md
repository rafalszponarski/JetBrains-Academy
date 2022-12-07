# Steps needed to complete project "[**_Honest Calculator_**](https://hyperskill.org/projects/208)"

## <br/>Stage 1:
### _Data collection_
We will start by implementing the flowchart below. Copy the messages carefully and assign them to the program variables. It makes no difference whether you make a list or each message is a separate variable. The appropriate messages must be displayed according to the flowchart. 

![flowchart stage 1](https://ucarecdn.com/b1770719-2eea-4389-b126-9fbd2edf8d96/)

&nbsp;

Implement the flowchart above. Please, follow our recommendations:

- The variable `calc` should have the following format: `x operation y`. For example: `2 + 3`, `2 + g` or `3.1 r 5`; 
- The variables `x` and `y` must be of the `float` or `int` type. The `oper` variable is a one-character string. Check whether the passed values have proper types. The delimiter must be a dot; 
- Copy the messages below carefully. The tests will check if the correct message appears in the correct order. Please, do not add extra lines or characters.

```
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Enter an equation
> 2 + m
Do you even know what numbers are? Stay focused!
Enter an equation
> 3 n 3
Yes ... an interesting math operation. You've slept through all classes, haven't you?
Enter an equation
> m - 2
Do you even know what the numbers are? Stay focused!
Enter an equation
> 4.7 * 5.2
```

## <br/>Stage 2:
### _First calculations_
In this stage, we will continue with the flowchart. Note that the blocks from the previous stage are in red. Be careful; some flows can work differently.

![flowchart stage 2](https://ucarecdn.com/14a82832-1487-4df0-8e1c-1893247d5193/)

&nbsp;

Implement the flowchart above. While doing it, please, follow our recommendations:

- Don't use the built-in functions to calculate from a string; 
  - The `result` variable must be of the `float` type; 
- Copy the message. The tests will check if the correct message appears in the correct order. So don't add extra lines or characters: `msg_3 = "Yeah... division by zero. Smart move..."`

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
Enter an equation
> 2 + m
Do you even know what numbers are? Stay focused!
Enter an equation
> 3 n 3
Yes ... an interesting math operation. You've slept through all classes, haven't you?
Enter an equation
> 4 / 0
Yeah... division by zero. Smart move...
Enter an equation
> 4 * 5.2
20.8
```

**Example 2:**
```
Enter an equation
> 411 - 211
200.0
```

## <br/>Stage 3:
### _Total recall_
Take a look at the upgraded flowchart. As before, the old blocks are red-colored. Be careful; some flows can now work differently.

![flowchart stage 3](https://ucarecdn.com/4a899d94-c524-48f1-8bfe-04ea9139172b/)

&nbsp;

To complete this stage, you need to implement the flowchart above. While doing it, please, follow our recommendations below:

- Don't use the built-in functions to calculate from a string; 
- The `memory` variable must be of a float type; use this variable to store intermediate result; 
- There are no tests when `M` is negative. For example, there will be no test input like this: `-M + 6`; 
- Copy two messages. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.

```
msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Enter an equation
> 3 + 3
6
Do you want to store the result? (y / n):
>y
Do you want to continue calculations? (y / n):
>y
Enter an equation
> 5 + M
11
Do you want to store the result? (y / n):
>y
Do you want to continue calculations? (y / n):
>n
```

## <br/>Stage 4:
### _The laziness test_
Implement the flowchart below. Take a good look — there're two functions. The old blocks are in red. Be careful; some flows can now work differently.

![flowchart stage 4](https://ucarecdn.com/0706cb45-ffba-4f2e-ab19-ab635467da58/)

Functions:
![functions stage 4](https://ucarecdn.com/74e59427-a12d-4d48-8c7c-29008d46503b/)

&nbsp;

Implement the flowchart with two functions. Please, mind the recommendations below:

- Don't use the built-in functions to calculate from a string; 
- Notice that the function `is_one_digit()` is supposed to check whether it has an integer value in the mathematical sense, e.g. 3.0 is an integer, 3.1 is a non-integer number. Thus, do NOT check the type of variable, but the number itself. You can use a special built-in method `.is_integer()` on a float variable to check if a number is an integer. 
- Copy the messages carefully. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.

```
msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Enter an equation
> 2 / M
You are ... lazy
Yeah... division by zero. Smart move...
Enter an equation
> 1 * M
You are ... lazy ... very lazy ... very, very lazy
0.0
Do you want to store the result? (y / n):
> n
Do you want to continue calculations? (y / n):
> y
Enter an equation
> 899 * 0
You are ... very, very lazy
0.0
Do you want to store the result? (y / n):
> n
Do you want to continue calculations? (y / n):
> n
```

## <br/>Stage 5:
### _Saving memory_
To complete the project, you need to implement the flowchart below. The old blocks are red-colored. Be careful; some flows can work differently. The functions from the previous stage have not been changed.

![flowchart stage 5](https://ucarecdn.com/5a9953cf-380a-4a12-a88b-bb45edd5e890/)

&nbsp;

Implement the flowchart. Please, follow the recommendations below:

- Don't use the built-in functions to calculate from a string; 
- Copy the messages below. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.

```
msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Enter an equation
2 + 3
You are ... lazy
5.0
Do you want to store the result? (y / n):
y
Are you sure? It is only one digit! (y / n)
y
Don't be silly, it's just one number! Add to the memory? (y / n)
n
Do you want to continue calculations? (y / n):
y
Enter an equation
5 + M
You are ... lazy ... very, very lazy
5.0
Do you want to store the result? (y / n):
y
Are you sure? It is only one digit! (y / n)
y
Don't be silly, it's just one number! Add to memory? (y / n)
y
Last chance! Do you really want to embarrass yourself? (y / n)
y
Do you want to continue calculations? (y / n):
y
Enter an equation
M / M
You are ... lazy
1.0
Do you want to store the result? (y / n):
n
Do you want to continue calculations? (y / n):
n
```
