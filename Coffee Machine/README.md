# Steps needed to complete project "[**_Coffee Machine_**](https://hyperskill.org/projects/68)"

## <br/>Stage 1:
### _Making coffee_
Let's start with a program that makes you a coffee – virtual coffee, of course. In this project, you will implement functionality that simulates a real coffee machine. It can run out of ingredients, such as milk or coffee beans, it can offer you various types of coffee, and, finally, it will take money for the prepared drink.

&nbsp;

The first version of the program just makes you a coffee. It should print to the standard output what it is doing as it makes the drink.

&nbsp;

Take a look at the sample output below and print all the following lines.

**Output:**
```
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
```

## <br/>Stage 2:
### _Ingredient calculator_
Now let's consider a case when you need a lot of coffee. Maybe you're hosting a party with a lot of guests! In these circumstances, it's better to make preparations in advance.

So, we will ask a user to enter the desired amount of coffee, in cups. Given this, you can adjust the program by calculating how much water, coffee, and milk are necessary to make the specified amount of coffee.

Of course, all this coffee is not needed right now, so at this stage, the coffee machine doesn't actually make any coffee yet.

&nbsp;

Let's break the task into several steps:

1. First, read the numbers of coffee drinks from the input. 
2. Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans. 
3. Output the required ingredient amounts back to the user.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** a dialogue with a user might look like this
```
Write how many cups of coffee you will need:
> 25
For 25 cups of coffee you will need:
5000 ml of water
1250 ml of milk
375 g of coffee beans
```

**Example 2:** here is another dialogue
```
Write how many cups of coffee you will need:
> 125
For 125 cups of coffee you will need:
25000 ml of water
6250 ml of milk
1875 g of coffee beans
```

## <br/>Stage 3:
### _Estimate the number of servings_
A real coffee machine doesn't have an infinite supply of water, milk, or coffee beans. And if you input a really big number, it's almost certain that a real coffee machine wouldn't have the supplies needed to make all that coffee for you.

In this stage, you need to improve the previous program. Now you will check amounts of water, milk, and coffee beans available in your coffee machine at the moment.

&nbsp;

Write a program that does the following:

1. It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs. 
2. If the coffee machine has enough supplies to make the specified amount of coffee, the program should print `"Yes, I can make that amount of coffee"`. 
3. If the coffee machine can make more than that, the program should output `"Yes, I can make that amount of coffee (and even N more than that)"`, where N is the number of additional cups of coffee that the coffee machine can make. 
4. If the amount of given resources is not enough to make the specified amount of coffee, the program should output `"No, I can make only N cups of coffee"`.

Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
Write how many ml of water the coffee machine has:
> 300
Write how many ml of milk the coffee machine has:
> 65
Write how many grams of coffee beans the coffee machine has:
> 100
Write how many cups of coffee you will need:
> 1
Yes, I can make that amount of coffee
```

**Example 2:**
```
Write how many ml of water the coffee machine has:
> 500
Write how many ml of milk the coffee machine has:
> 250
Write how many grams of coffee beans the coffee machine has:
> 200
Write how many cups of coffee you will need:
> 10
No, I can make only 2 cups of coffee
```

**Example 3:**
```
Write how many ml of water the coffee machine has:
> 1550
Write how many ml of milk the coffee machine has:
> 299
Write how many grams of coffee beans the coffee machine has:
> 300
Write how many cups of coffee you will need:
> 3
Yes, I can make that amount of coffee (and even 2 more than that)
```

**Example 4:**
```
Write how many ml of water the coffee machine has:
> 0
Write how many ml of milk the coffee machine has:
> 0
Write how many grams of coffee beans the coffee machine has:
> 0
Write how many cups of coffee you will need:
> 1
No, I can make only 0 cups of coffee
```

**Example 5:**
```
Write how many ml of water the coffee machine has:
> 0
Write how many ml of milk the coffee machine has:
> 0
Write how many grams of coffee beans the coffee machine has:
> 0
Write how many cups of coffee you will need:
> 0
Yes, I can make that amount of coffee 
```

**Example 6:**
```
Write how many ml of water the coffee machine has:
> 200
Write how many ml of milk the coffee machine has:
> 50
Write how many grams of coffee beans the coffee machine has:
> 15
Write how many cups of coffee you will need:
> 0
Yes, I can make that amount of coffee (and even 1 more than that)
```

## <br/>Stage 4:
### _Buy, fill, take!_
Let's simulate an actual coffee machine! What do we need for that? This coffee machine will have a limited supply of water, milk, coffee beans, and disposable cups. Also, it will calculate how much money it gets for selling coffee.

There are several options for the coffee machine we want you to implement: first, it should sell coffee. It can make different types of coffee: espresso, latte, and cappuccino. Of course, each variety requires a different amount of supplies, however, in any case, you will need only one disposable cup for a drink. Second, the coffee machine must get replenished by a special worker. Third, another special worker should be able to take out money from the coffee machine.

&nbsp;

Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program is supposed to do one of the mentioned actions at a time. It should also calculate the amounts of remaining ingredients and how much money is left. Display the quantity of supplies before and after purchase.

1. First, your program reads one option from the standard input, which can be `"buy"`, `"fill"`, `"take"`. If a user wants to buy some coffee, the input is `"buy"`. If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be `"fill"`. If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input `"take"`. 
2. If the user writes `"buy"` then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.
   - For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
   - For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
   - And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
3. If the user writes `"fill"`, the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine. 
4. If the user writes `"take"` the program should give all the money that it earned from selling coffee.

At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.

To sum up, your program should print the coffee machine's state, process one query from the user, as well as print the coffee machine's state after that. Try to use functions for implementing every action that the coffee machine can do.

&nbsp;

An espresso should be number 1 in the list, a latte number 2, and a cappuccino number 3.
Options are named as `"buy"`, `"fill"`, `"take"`.

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take): 
> buy
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: 
> 3

The coffee machine has:
200 ml of water
440 ml of milk
108 g of coffee beans
8 disposable cups
$556 of money
```

**Example 2:**
```
The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take): 
> fill
Write how many ml of water you want to add: 
> 2000
Write how many ml of milk you want to add: 
> 500
Write how many grams of coffee beans you want to add: 
> 100
Write how many disposable cups you want to add: 
> 10

The coffee machine has:
2400 ml of water
1040 ml of milk
220 g of coffee beans
19 disposable cups
$550 of money
```

**Example 3:**
```
The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take): 
> take
I gave you $550

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$0 of money
```

## <br/>Stage 5:
### _Keep track of the supplies_
Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. It should repeatedly ask a user what they want to do. If the user types `"buy"`, `"fill"` or `"take"`, then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, they should type `"exit"`. The program should terminate on this command. Also, when the user types `"remaining"`, the program should output all the resources that the coffee machine has. This means that you shouldn't show the remaining stock levels at the beginning/end of the program.

Remember, that:

- For the espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4. 
- For the latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7. 
- And for the cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.

&nbsp;

Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: `"remaining"` and `"exit"`.

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee and state what is missing.

And the last improvement to the program at this step — if the user types `"buy"` to buy a cup of coffee and then changes his mind, they should be able to type `"back"` to return into the main cycle.

&nbsp;

Your coffee machine should have the same initial resources as in the example (400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash).

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
Write action (buy, fill, take, remaining, exit): 
> remaining

The coffee machine has:
400 ml of water
540 ml of milk
120 g of coffee beans
9 disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit): 
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: 
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit): 
> remaining

The coffee machine has:
50 ml of water
465 ml of milk
100 g of coffee beans
8 disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit): 
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: 
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit): 
> fill

Write how many ml of water you want to add: 
> 1000
Write how many ml of milk you want to add: 
> 0
Write how many grams of coffee beans you want to add: 
> 0
Write how many disposable cups you want to add: 
> 0

Write action (buy, fill, take, remaining, exit): 
> remaining

The coffee machine has:
1050 ml of water
465 ml of milk
100 g of coffee beans
8 disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit): 
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: 
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit): 
> remaining

The coffee machine has:
700 ml of water
390 ml of milk
80 g of coffee beans
7 disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit): 
> take

I gave you $564

Write action (buy, fill, take, remaining, exit): 
> remaining

The coffee machine has:
700 ml of water
390 ml of milk
80 g of coffee beans
7 disposable cups
$0 of money

Write action (buy, fill, take, remaining, exit): 
> exit
```

## <br/>Stage 6:
### _Brush up your code_
Let's redesign our program and write a class that represents a coffee machine. The class should have a method that takes a string as input. Every time the user inputs a string to the console, the program invokes this method with one argument: the line that the user inputs to the console. This system simulates pretty accurately how real-world electronic devices work. External components (like buttons on the coffee machine or tapping on the screen) generate events that pass into the single interface of the program.

The class should not use system input at all; it will only handle the input that comes to it via this method and its string argument.

The first problem that comes to mind: how to write that method in a way that it represents all that coffee machine can do? If the user inputs a single number, how can the method determine what that number is: a variant of coffee chosen by the user or the number of the disposable cups that a special worker added into the coffee machine?

The right solution to this problem is to store the current state of the machine. The coffee machine has several states it can be in. For example, the state could be "choosing an action" or "choosing a type of coffee". Every time the user inputs something and a program passes that line to the method, the program determines how to interpret this line using the information about the current state. After processing this line, the state of the coffee machine can be changed or can stay the same.

Remember, that:

- For the espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4. 
- For the latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7. 
- And for the cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.

&nbsp;

Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method.

&nbsp;

Your coffee machine should have the same initial resources as in the example (400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash).
The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```

```
