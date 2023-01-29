# Steps needed to complete project "[**_Hangman_**](https://hyperskill.org/projects/69)"

## <br/>Stage 1:
### _Hello, Hangman_
Hangman is a popular, funny, yet very grim game. A cruel computer hides a word from you and you need to guess it, letter by letter. If you fail, you'll be hanged, if you win, you'll survive.

You're probably familiar with the rules; now you can create this game yourself!

Let's take a brief look at what you are going to build in this project. Here is what the gameplay will look like:

- In the main menu, players can choose to either play or exit the game; 
- If players choose to play, the computer picks a word from a list — it will be the answer; 
- The computer asks players to enter a letter that may or may not be in the word; 
- If players suggest a letter that does not appear in the word for the first time, It's a miss. A player can miss 8 times before the game is over; 
- If the letter does occur in the word, the computer notifies the players. If there are letters left to guess, the computer invites the player to go on; 
- When the entire word is uncovered — it's a victory! The game should calculate the final score and return to the main menu.

This may sound complex, but the project is split into small stages with the hints that will guide you. We guarantee that the final product is replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print with Python. Apply that knowledge to entice your friends to play with an announcement for your game!

&nbsp;

In this stage, write a program that prints the lines shown in the example below.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
H A N G M A N
The game will be available soon.
```


## <br/>Stage 2:
### _Let’s play a game_
In this stage, we will add some simple gameplay. There will be two possible outcomes. Let's first print a welcoming message and then ask players to guess the word we have set for the game. If they guess the word, the game reports a win; otherwise, it will "hang" the player.

&nbsp;

- Ask players for a possible word; 
- Print You survived! if users guess the word; 
- Print You lost! if users fail.

> In this stage, python is the word that players need to guess. For now, this is the only form of answer that is deemed correct, so there is no need to worry about the register or punctuation marks.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
H A N G M A N
Guess the word: > python
You survived!
```

**Example 2:**
```
H A N G M A N
Guess the word: > java
You lost!
```


## <br/>Stage 3:
### _Make your choice_
If there is only one word, the game becomes dull. You already know the word, and there’s no challenge. In this stage, let's make the game more difficult by choosing a word from the special list with a variety of options. This way, our game gains in replayability.

&nbsp;

- Create the following list of words: `python`, `java`, `swift`, `javascript`; 
- Program the game to choose a word from the list at random (you can use the `random` library for that). You can enter more words, but let's stick to these four for now.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** computer chooses python from the list
```
H A N G M A N
Guess the word: > python
You survived!
```

**Example 2:** computer chooses something other than python from the list
```
H A N G M A N
Guess the word: > python
You lost!
```

**Example 3:** computer randomly chooses something other than swift from the list
```
H A N G M A N
Guess the word: > swift
You lost!
```


## <br/>Stage 4:
### _Help is on the way_
The game is now more difficult to beat; your chances of guessing the word depend on the list size. If there are four words in the list, you have a 25% chance. Let's show a little mercy and add hints for our players.

&nbsp;

- As in the previous stage, use the following word list: `python`, `java`, `swift`, `javascript`; 
- Once the computer has chosen a word from the list, show its first three letters. Replace the hidden letters with hyphens (`-`).

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
H A N G M A N
Guess the word jav-: > java
You survived!
```

**Example 2:**
```
H A N G M A N
Guess the word pyt---: > pythia
You lost!
```


## <br/>Stage 5:
### _Keep trying_
Let's make the game iterative. In this stage, we'll adjust our game to resemble the classic version of Hangman. Players should now guess the letters in a word instead of inputting an entire word. If an attempt is successful, uncover the letter. We also need to add the lose condition — players have eight attempts to guess all letters that appear in the word. When players run out of attempts, the game ends.

Don't forget to get rid of the hints: replace all the letters in a word with hyphens at the beginning. Players input one lowercase letter at a time, so there is no need to worry about that.

Later on, we will also determine the win conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

&nbsp;

Your game should work as follows:

- Players have exactly eight attempts to guess the word by entering letters one by one. Asking for a letter, print: `Input a letter:`. If a player uncovered all the letters, but some attempts are still left, the program must continue to ask for input until all the tries are exhausted; 
- If the letter doesn't appear in the word, the computer takes one try away – even if a user has already suggested this letter – and prints `That letter doesn't appear in the word.`; 
- If the letter does appear in the word but a user has already suggested this letter and it's open, no need to print any messages; 
- If all attempts are exhausted, the game ends; the program shows a final message (`Thanks for playing!`). Otherwise, players can continue to input letters; 
- We continue to stick with the word list from the previous stage: `python`, `java`, `swift`, `javascript`. It ensures that your program is tested reliably. Don't worry about `javascript`. Yes, it's longer than 8 characters, but we'll keep it in the list for consistency since we're not done with developing the game yet and for now there is no win or lose.

> Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.  Comments after `#` provided for illustrative purposes and not as part of the task.

**Example 1:**
```
H A N G M A N  # 8 attempts

----------
Input a letter: > a  # 7 attempts

-a-a------
Input a letter: > i  # 6 attempts

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word.  # 5 attempts

-a-a---i--
Input a letter: > z
That letter doesn't appear in the word.  # 4 attempts

-a-a---i--
Input a letter: > l
That letter doesn't appear in the word.  # 3 attempts

-a-a---i--
Input a letter: > p  # 2 attempts

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word.  # 1 attempt

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word.  # 0 attempts

Thanks for playing!
```

**Example 2:**
```
H A N G M A N  # 8 attempts

----
Input a letter: > j  # 7 attempts

j---
Input a letter: > i
That letter doesn't appear in the word.  # 6 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 5 attempts

j---
Input a letter: > o
That letter doesn't appear in the word.  # 4 attempts

j---
Input a letter: > a  # 3 attempts

ja-a
Input a letter: > v  # 2 attempts

java
Input a letter: > a  # 1 attempt

java
Input a letter: > j  # 0 attempts

Thanks for playing!
```


## <br/>Stage 6:
### _The value of life_
So far, our game has been some kind of a draft; we still lack a way to handle the player's victory. The player has only eight attempts, and the number of remaining attempts decreases every turn, even if players guess them correctly.

In this stage, we will start reducing the attempts only after players make a mistake. They can be mistaken eight times: attempts are reduced if the suggested letter is not in the word or if it has already been suggested before (no matter whether it's been a correct one or not). If a player has guessed all the letters, they win. If a player has some attempts after guessing the word, discard them, notify the player, and terminate the game.

&nbsp;

Players start the game with eight lives. In other words, they can make a mistake only eight times.

- When players input a valid letter, uncover it in the word, and carry on; 
- Print `That letter doesn't appear in the word.` and reduce the number of attempts if the word doesn't contain the letter, even if this particular letter has already been suggested before;
- Print `No improvements.` and reduce the attempt' counter when players input a letter that has been successfully uncovered before; 
- When players win, print the uncovered word, `You guessed the word!` , and the winning message. Each one should be on a new line.

> Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input. Comments after `#` provided for illustrative purposes and not as part of the task.

**Example 1:** note how the attempts are decreased when the player inputs the same letter twice or thrice
```
H A N G M A N  # 8 attempts

------
Input a letter: > t

--t---
Input a letter: > z
That letter doesn't appear in the word.  # 7 attempts

--t---
Input a letter: > t
No improvements.  # 6 attempts

--t---
Input a letter: > t
No improvements.  # 5 attempts

--t---
Input a letter: > y

-yt---
Input a letter: > x
That letter doesn't appear in the word.  # 4 attempts

-yt---
Input a letter: > y
No improvements.  # 3 attempts

-yt---
Input a letter: > p

pyt---
Input a letter: > p
No improvements.  # 2 attempts

pyt---
Input a letter: > q
That letter doesn't appear in the word.  # 1 attempt

pyt---
Input a letter: > p
No improvements.  # 0 attempts

You lost!
```

**Example 2:** success
```
H A N G M A N  # 8 attempts

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word.  # 7 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 6 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 5 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 4 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 3 attempts

j---
Input a letter: > a

ja-a
Input a letter: > v

java
You guessed the word!
You survived!
```


## <br/>Stage 7:
### _Error!_
The skeleton of the game is ready; let's put some more gameplay meat on it.

In the previous stage, if players entered the same letter twice or more, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. This doesn’t seem fair, right? Players gain nothing, and the number of attempts gets smaller. Let's fix it!

&nbsp;

To complete this stage, follow the suggested order of the required checks:

- Check whether players enter exactly one letter. If not, print `Please, input a single letter.`. Remember that when players input nothing or non-letter characters, it shouldn't count as a correct input either; 
- Make sure that the player entered a lowercase English letter. If not, the program should print `Please, enter a lowercase letter from the English alphabet.`; 
- If users enter the same letter twice (doesn't matter whether it appears in the word or not), then the program should output `You've already guessed this letter.`. Do not decrease the number of attempts in this case; 
- None of the three errors described above should reduce the number of remaining attempts! 
- When players win, print `You guessed the word <word>!`, where `<word>` should be substituted with the uncovered word, and the winning message. Each one should be on a new line.

> Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.  Comments after # provided for illustrative purposes and not as part of the task.

**Example 1:**
```
H A N G M A N  # 8 attempts

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word.  # 7 attempts

-a-a---i--
Input a letter: > o
You've already guessed this letter.

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You've already guessed this letter.

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word.  # 6 attempts

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word.  # 5 attempts

-a-a---ip-
Input a letter: > a
You've already guessed this letter.

-a-a---ip-
Input a letter: > z
That letter doesn't appear in the word.  # 4 attempts

-a-a---ip-
Input a letter: > t

-a-a---ipt
Input a letter: > x
That letter doesn't appear in the word.  # 3 attempts

-a-a---ipt
Input a letter: > b
That letter doesn't appear in the word.  # 2 attempts

-a-a---ipt
Input a letter: > d
That letter doesn't appear in the word.  # 1 attempt

-a-a---ipt
Input a letter: > w
That letter doesn't appear in the word.  # 0 attempts

You lost!
```

**Example 2:**
```
H A N G M A N  # 8 attempts

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word.  # 7 attempts

j---
Input a letter: > +
Please, enter a lowercase letter from the English alphabet.

j---
Input a letter: > A
Please, enter a lowercase letter from the English alphabet.

j---
Input a letter: > ii
Please, input a single letter.

j---
Input a letter: > ++
Please, input a single letter.

j---
Input a letter: >
Please, input a single letter.

j---
Input a letter: > g
That letter doesn't appear in the word.  # 6 attempts

j---
Input a letter: > a

ja-a
Input a letter: > v
You guessed the word java!
You survived!
```


## <br/>Stage 8:
### _Menu, please_
In this stage, let's add a little more flavor to the game by constructing a menu to restart the program after the current session ends.

&nbsp;

- The game now starts with the menu where players can choose to either play, see their score, or exit; 
- Print `Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:` and show this message again if players input something else; 
- If players choose `play`, start the game. When the game is finished (regardless of whether a player wins or not), pop up the menu once again to make the gameplay seamless; 
- If players choose `results`, print how many games they won, e.g. `You won: 0 times`, and how many games they lost, e.g. `You lost: 25 times`; 
- If players choose `exit`, end the game.

> Please, make sure that the output format of your program follows the example precisely. Pay attention to the empty lines between attempts and at the end.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.  Comments after # provided for illustrative purposes and not as part of the task.

**Example:**
```
H A N G M A N  # 8 attempts
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > play

------
Input a letter: > h

---h--
Input a letter: > K
Please, enter a lowercase letter from the English alphabet.

---h--
Input a letter: > t

--th--
Input a letter: > o

--tho-
Input a letter: > +
Please, enter a lowercase letter from the English alphabet.

--tho-
Input a letter: > K
Please, enter a lowercase letter from the English alphabet.

--tho-
Input a letter: > h
You've already guessed this letter.

--tho-
Input a letter: > K
Please, enter a lowercase letter from the English alphabet.

--tho-
Input a letter: > n

--thon
Input a letter: > q
That letter doesn't appear in the word.  # 7 attempts

--thon
Input a letter: > y

-ython
Input a letter: > h
You've already guessed this letter.

-ython
Input a letter: > p

You guessed the word python!
You survived!
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > results
You won: 1 times.
You lost: 0 times.
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > exit
```
