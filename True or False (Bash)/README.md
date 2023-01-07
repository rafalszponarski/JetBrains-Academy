# Steps needed to complete project "[**_True or False_**](https://hyperskill.org/projects/294)"

## <br/>Stage 1:
### _Invitation_
Before retrieving data from the API, you need to learn your username and password. Connect to the given endpoint and download your ID card. Then print the content of the ID card to the standard output.

&nbsp;

Let's break the task into several steps:

- Print the welcoming message: `Welcome to the True or False Game!`; 
- Use `curl`, connect to the endpoint `http://0.0.0.0:8000/download/file.txt`, and download the file as ID_card.txt; 
- Use the `--silent` option to avoid the terminal messages; 
- Use the `--output <filename>` option to name the output file; 
- Print the content of ID_card.txt to the standard output;

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Welcome to the True or False Game!
{"username": "the_username", "password": "the_password"}
```


## <br/>Stage 2:
### _Access granted_
You know your username and password. In this stage, connect to the endpoint with the username and password, grant access, and save your session cookie.

&nbsp;

Let's break the task into several steps:

- Print the welcoming message: `Welcome to the True or False Game!`; 
- Use `curl` to connect to the endpoint `http://0.0.0.0:8000/login` and save your session cookie as cookie.txt; 
- Use the `--silent` option to avoid the terminal messages; 
- Use the `--cookie-jar <cookie_name>` option to name the cookie; 
- Use the `--user <username:password>` option to authenticate. You know your username and password from the previous stage; 
- Print the login message: `Login message: the-message-from-endpoint`

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Welcome to the True or False Game!
Login message: L***** ** ************!
```


## <br/>Stage 3:
### _That is the question_
Time to get a question from the API. Connect to the given endpoint with your session cookie and get a question. Print the question to the standard output.

&nbsp;

Let's break the task into several steps:

- Keep functionality from the previous steps; 
- Use curl to connect to the endpoint `http://0.0.0.0:8000/game` by sending your session cookie `cookie.txt`; 
- Use the `--cookie <cookie_name>` option to send the cookie; 
- The endpoint will respond to you with a question and the answer; 
- Print the response to the standard output. `Response: {"question": "the-question-from-endpoint", "answer": "the-answer-from-endpoint"}`;

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
Welcome to the True or False Game!
Login message: Logged in successfully!
Response: {"question": "The Sun is 109 times wider than Earth", "answer": "True"}
```


**Example 2:**
```
Welcome to the True or False Game!
Login message: Logged in successfully!
Response: {"question": "Rihanna is a rugby player", "answer": "False"}
```

**Example 3:**
```
Welcome to the True or False Game!
Login message: Logged in successfully!
Response: {"question": "Illidan Stormrage betrayed his own clan", "answer": "True"}
```

## <br/>Stage 4:
### _Menu_
Now, you need to create the main menu for your program.

&nbsp;

Let's break the task into several steps:

- Start with the message Welcome to the `True or False Game!` 
- Print out the menu and ask for an option:
```
    0. Exit
    1. Play a game
    2. Display scores
    3. Reset scores
    Enter an option:
```

- Read the option from the standard input;

- If the option is not found:
  - Print `Invalid option!`
  - Return to the main menu;

- If the option is `1`:
  - Print `Playing game`;
  - Return to the main menu;

- If the option is `2`:
  - Print `Displaying scores`;
  - Return to the main menu;

- If the option is `3`:
  - Print `Resetting scores`;
  - Return to the main menu;

- If the option is `0`:
  - Print, `See you later!` and exit the program.


&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 7
Invalid option!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 1
Playing game

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 2
Displaying scores

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 3
Resetting scores

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```


## <br/>Stage 5:
### _The game is on_
In this stage, create the game functionality. Start by asking the player's name. Loop the game until the answer is wrong. Display the score when a game ends.

&nbsp;

Let's break the task into several steps:

- Keep the functionality from the previous steps;
- Print out the menu and ask for an option;
- If the option is `1`:
  - Ask for the player's name with `What is your name?`
  - Use the `RANDOM` function to generate random numbers. For testing purposes, start each game with a seed value. `RANDOM=4096`;
  - Connect to the `/game` endpoint of the API to retrieve a question and an answer;
  - Print the question to the standard output;
  - Ask if it is `True or False?`;
  - Read the user response from the standard input;
  - Compare it with the answer from the endpoint;
  - If the answers match:
    - The player wins ten score points. Store them;
    - Select a random word from the list with the help of the `RANDOM` function `( "Perfect!" "Awesome!" "You are a genius!" "Wow!" "Wonderful!" )` and print to the standard output;
    - Repeat until the player's answer is wrong;
  - If the answer is wrong:
    - Print `Wrong answer, sorry!`;
    - Print `<player_name> you have <number_of_correct_answers> correct answer(s).`;
    - Print `Your score is <score> points.`;
    - Return to the main menu;
- If the option is `0`:
  - Print `See you later!` and exit from the program

You can parse a key from the JSON string with the help of the `sed` command. The code snippet below shows an example of it:
```
item="the-question-answer-item-from-the-API"
question=$(echo "$item" | sed 's/.*"question": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
```
As an alternative, if you have `Python3`, you can use the code snippet below:
```
item="the-question-answer-item-from-the-API"
question=$(python3 -c "data=$item; print(data.get('question'))
```
You can pick a random element from a list with the help of the `RANDOM` function. The code snippet below shows an example of it:
```
idx=$((RANDOM % 5))
echo "${responses[$idx]}"
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 5
Invalid option!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 2
Displaying scores

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 3
Resetting scores

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```

**Example 2:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 1
What is your name?
> hyper

Bright brothers had invented the first successful airplane
True or False?
> False
You are a genius!

The International Space Station circles the globe every 900 minutes
True or False?
> False
Wonderful!

The Sun is 109 times wider than Earth
True or False?
> True
Awesome!

John Bardeen - Walter Brattain - William Shockley invented the first working transistors at Bell Labs
True or False?
> False
Wrong answer, sorry!
hyper you have 3 correct answer(s).
Your score is 30 points.

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```


## <br/>Stage 6:
### _I am the best_
In this stage, we will continue working on the menu. Store the game score of each game.

&nbsp;

Let's break the task into several steps:

- Keep the functionality from the previous steps;
- Save the player's score in the scores.txt file;
- Use the format `User: hyper, Score: 20, Date: 2022-04-23` and add each new score line to the end of the score file;
- Print out the menu and ask for an option;
- If the option is `2`:
  - If the score file is found:
    - Print `Player scores` as the header;
    - Then print the scores to the standard output;
  - If the file is not found or there are no scores inside:
    - Print `File not found or no scores in it!`;
- If the option is `3`:
  - If the score file is found:
    - Delete the `scores.txt`;
    - Display message `File deleted successfully!`;
    - `scores.txt` should not exist after deletion;
  - If the file is not found or there are no scores inside:
    - Print `File not found or no scores in it!`;
- If the option is `0`:
  - Print `See you later!` and exit from the program

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 2
File not found or no scores in it!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 3
File not found or no scores in it!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```

**Example 2:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 1
What is your name?
> hyper

Pong is the first commercially successful video game
True or False?
> True
You are a genius!

The first mechanical computer - The Babbage Difference Engine - was designed by Charles Babbage in 1922
True or False?
> False
Wonderful!

Rihanna is a rugby player
True or False?
> False
Awesome!

Bright brothers had invented the first successful airplane
True or False?
> False
You are a genius!

The heaviest land mammal is the African bush elephant
True or False?
> False
Wrong answer, sorry!
hyper you have 4 correct answer(s).
Your score is 40 points.

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 1
What is your name?
> jet

The International Space Station circles the globe every 900 minutes
True or False?
> False
You are a genius!

The Sun is 109 times wider than Earth
True or False?
> True
Wonderful!

John Bardeen - Walter Brattain - William Shockley invented the first working transistors at Bell Labs
True or False?
> False
Wrong answer, sorry!
jet you have 2 correct answer(s).
Your score is 20 points.

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```

**Example 3:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 2
Player scores
User: hyper, Score: 40, Date: 2022-05-08
User: jet, Score: 20, Date: 2022-06-19

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```

**Example 4:**
```
Welcome to the True or False Game!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 3
File deleted successfully!

0. Exit
1. Play a game
2. Display scores
3. Reset scores
Enter an option:
> 0
See you later!
```
