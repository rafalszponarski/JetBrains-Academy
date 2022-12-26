# Steps needed to complete project "[**_Bill Splitter_**](https://hyperskill.org/projects/175)"

## <br/>Stage 1:
### _Invite your friends_
You have planned a dinner with your friends today. It's the right time to add them to your program. You need to be sure how many friends are joining you for dinner including you.

The idea is to take names from user input. Store them in a dictionary.

For example, if five friends are joining including you, you need to add five people to the dictionary so that you can access/update the corresponding bill value later.

&nbsp;

In this stage your program should perform the following steps:

1. Take user input — how many people want to join, including the user; 
2. In case of an invalid number of people (zero or negative), `"No one is joining for the party"` is expected as an output; 
3. Otherwise, take the friends' names as input, iteratively; 
4. Store them in a dictionary initialized with zeros; 
5. Print out the dictionary.

To communicate with the user, please use the prompts specified in the examples. Note that here and in the following stages we expect you to take every input in a new line.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** Valid input
```
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

{'Marc': 0, 'Jem': 0, 'Monica': 0, 'Anna': 0, 'Jason': 0}
```

**Example 2:** Invalid input
```
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```

## <br/>Stage 2:
### _The bill has arrived_
It's bill time! Let's split the bill among everyone and update the values in the dictionary you have created in the previous stage.

Since we don't want to deal with too many decimals (who carries that much change anyway?), round the split amount to two decimal places and then update the dictionary with the split values.

&nbsp;

In this stage your program should perform the following steps together with the steps of the previous stage:

1. If there are no people to split the bill (the number of friends is 0 or an invalid input), output `"No one is joining for the party"`; 
2. Else, take user input: the final bill; 
3. Split the total bill equally among everyone; 
4. Round the split value to two decimal places; 
5. Update the dictionary with the split values; 
6. Print the updated dictionary.

Do not print the output of the previous stage (see examples).

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** Five people joining
```
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
```

**Example 2:** Seven people joining
```
Enter the number of friends joining (including you):
> 7

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
> Ben
> Ned

Enter the total bill value:
> 41

{'Marc': 5.86, 'Jem': 5.86, 'Monica':5.86, 'Anna': 5.86, 'Jason': 5.86, 'Ben': 5.86, 'Ned': 5.86}
```

**Example 3:** Invalid input
```
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```

## <br/>Stage 3:
### _The Lucky One_
In this stage, you need to add a new feature to the project — pick one name from the dictionary at random; this person's share will be paid by others. Make it a lucky day for somebody!

Make sure you give your users a choice whether they want to use this feature or not. Don't turn it on by default.

After picking a random name, print it so that everyone knows who is the lucky one.

&nbsp;

In this stage your program should perform the following steps together with the steps from the previous stages:

1. In case of an invalid number of people, `"No one is joining for the party"` is expected as an output; 
2. Otherwise, ask the user whether they want to use the "Who is lucky?" feature; 
3. Take input from the user; 
4. If a user wants to use the feature (`Yes`), choose a name from the dictionary keys at random and print the following: `{Name} is the lucky one!`; 
5. If the user enters anything else, print `No one is going to be lucky`.

Do not print the output of the previous stage (see examples).

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** The feature is used
```
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!
```

**Example 2:** The feature is skipped
```
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky
```

**Example 3:** Invalid input
```
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```

## <br/>Stage 4:
### _Party is over_
It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better. First, we need to recalculate the split value for everyone. Make sure that our lucky one pays `0`.

Recalculate the split value for `n-1` people where `n` is the total length of the dictionary and update the values in the dictionary with the new split value for everyone.

If a user decides not to use the "Who is lucky" feature, print the original dictionary.

&nbsp;

In this stage your program should perform the following steps together with the steps from the previous stages:

1. In case of an invalid number of people, `"No one is joining for the party"` is expected as an output; 
2. Otherwise, if the user choice is `Yes`, re-split the bill according to the feature; 
3. Round the split value to two decimal places; 
4. Update the dictionary with new split values and `0` for the lucky person; 
5. Print the updated dictionary; 
6. If the user entered anything else instead of `Yes`, print the original dictionary.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** The feature is used
```
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}
```

**Example 2:** The feature is skipped
```
Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> No

No one is going to be lucky

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
```

**Example 3:** Invalid input
```
Enter the number of friends joining (including you):
> 0

No one is joining for the party
```
