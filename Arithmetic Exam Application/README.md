# Steps needed to complete project "[**_Arithmetic Exam Application_**](https://hyperskill.org/projects/173)"

## <br/>Stage 1:
### _Mini-calculator_
People learn new things in one way or another. Learning sometimes means that you need to check your comprehension by taking a test. It also requires a person (or a program) to check your answers. You may have been in a situation when you think that you have solved the task correctly, but your professor has a different (sometimes wrong!) answer. It happens; everybody makes mistakes.

Not our application though. It should calculate the solution in a very precise manner. We need to make a simple calculator that can evaluate expressions like `a + b`, `a - b`, or `a * b`. We will leave the division aside for now.

&nbsp;

1. A user inputs a line that looks like a simple mathematical operation.
2. The application should print the result of the operation.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> 5 + 7
12
```

**Example 2:**
```
> 3 * 100
300
```

**Example 3:**
```
> 5 - 10
-5
```

**Example 4:**
```
> 8 * 0
0
```

## <br/>Stage 2:
### _Task generator_
Any test includes at least one task. This task can vary in difficulty and required timeframes. There can be more than one task; they can demand different forms of answers. One thing remains — if there's a task, there's a solution. And we need to assess it.

Math tasks can vary in difficulty. `1 * 3` is easy. `75 * 34` is a bit more difficult. For the next stages, think about levels of difficulty that you can add!

For now, let's use random numbers from `2` to `9` and integer operations: `+`, `-` and `*`.

&nbsp;

1. Generate a math task that looks like a math operation. Use the requirements above. Print it. 
2. Read the answer from a user. 
3. Check whether the answer is correct. Print Right! or Wrong!

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
5 * 7
> 35
Right!
```

**Example 2:**
```
5 * 7
> 5
Wrong!
```

## <br/>Stage 3:
### _More tasks needed!_
Let's write an application that assesses the user's knowledge.
Many people get nervous during exams; they can accidentally hit a wrong key, confuse `,` with `.` in floats, and so on. Our application should allow some room for errors and give a person the opportunity to correct the typo.

&nbsp;

1. The application should give the user 5 tasks. The tasks are akin to the previous stage: two numbers from `2` to `9` and an integer operation. 
2. The user receives one task, prints the answer. If the answer contains a typo (letters or otherwise empty), the program should print `Incorrect format`. and ask to re-enter the answer. Repeat until the answer is in the correct format. If the answer is a number, print `Right!` or `Wrong!` depending on the answer and carry on to the next question. 
3. After five tasks, output `Your mark is n/5`. where n is the number of correct answers.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:** An example of the output
```
3 + 8
> 11q
Incorrect format.
> eleven
Incorrect format.
> 11
Right!
5 * 7
> 35
Right!
2 - 5
> -4
Wrong!
3 * 3
> 9
Right!
8 + 3
> 11
Right!
Your mark is 4/5.
```

## <br/>Stage 4:
### _Adding marks_
Simple tasks are good for younger kids, but math can be more difficult and more interesting! Quadratic equations, trigonometry, and a lot of other interesting things. Math library can help you with that.

Sometimes students want to save the results of the test. This is useful for viewing the learning dynamics on a topic or to identify difficult tasks.

At this stage, let's add integral squares. Of course, you can add more difficulty levels later.

&nbsp;

1. With the first message, the program should ask for a difficulty level:
    1 - simple operations with numbers 2-9
    2 - integral squares 11-29

2. A user enters an answer.
    For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
    For the second difficulty level: the task is an integer; the answer is the square of this number.
    In case of another input: ask to re-enter. Repeat until the format is correct.

3. The application gives 5 tasks to a user.

4. The user receives one task, prints the answer.
    If the answer contains a typo, print `Incorrect format`. and ask to re-enter the answer. Repeat until the answer is in the correct format.
    If the answer is a number, print `Right!` or `Wrong!` Go to the next question.

5. After five answers, print `Your mark is N/5`. where **N** is the number of correct answers.

6. Output `Would you like to save your result to the file? Enter yes or no`.
    In case of `yes`, `YES`, `y`, `Yes`: the app should ask the username and write `Name: n/5 in level X (<level description>)`. (X stands for the level number) in the `results.txt` file. For example — `Alex: 3/5 in level 1 (simple operations with numbers 2-9)`.
    The results should be saved to the file immediately after the user gave the positive answer to the question `Would you like to save your result to the file?`
    If the file `results.txt` does not exist, you should create it.

7. In case of `no` or any other word: exit the program.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:** An example of the output
```
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 11
Incorrect format.
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 2
11
> 121
Right!
15
> 100
Wrong!
21
> 441'
Wrong format! Try again.
21
> 441
Right!
17
> 289
Right!
13
> 169
Right!
Your mark is 4/5. Would you like to save the result? Enter yes or no.
> yes
What is your name?
> Kate
The results are saved in "results.txt".
```

&nbsp;

## Afterword

After finishing this stage, you are totally free to improve the project in any way you like to make it a more convenient and useful tool.

You can add any features to your application. It will not be verified by tests, so there are no strict requirements.

Sample ideas:

1. Add a complex exam. Increase a difficulty level on the fly. For example, if a person passed the 1st level, start the 2nd one immediately. 
2. You can add a correction level: store the tasks with wrong answers and give them next time. 
3. Add more difficulty levels. 
4. Track the time (read about Timer). 
5. Write a more detailed report to a file with the results. 
6. Show previous results inside the app (show lines from `results.txt` that contains the username) 
7. Any other improvement that might be useful!
