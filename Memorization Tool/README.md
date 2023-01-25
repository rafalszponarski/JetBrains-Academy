# Steps needed to complete project "[**_Memorization Tool_**](https://hyperskill.org/projects/159)"

## <br/>Stage 1:
### _Make your own flashcards_
A good memorizing tool can boost your short and long-term memory. If you tried to learn a foreign language, you probably know what a flashcard is. It is an excellent device to remember facts. Flashcards alone are not enough, we need a special technique.

Let's create our flashcards first. A flashcard is a piece of paper with a question on one side and the answer on the other. Let's assume we need to memorize the capital cities of various countries. Write the country name on one side and the capital on the other.

&nbsp;

In this stage, we need to create our first flashcards.
When the program starts, it should print the menu below. It is our main menu (1):

```
1. Add flashcards
2. Practice flashcards
3. Exit
```

If `1` is entered, the program should print the following sub-menu (2):

```
1. Add a new flashcard
2. Exit
```

By choosing the `Add a new flashcard` option, a user is prompted to enter a `Question` and an `Answer`. Once they are entered, the program automatically returns to the sub-menu (2). Iterate this process every time a user wants to add a new flashcard.

**Flashcard practice:**

The `Practice flashcards` option in the main menu (1) should print all the questions and answers that have been added previously. If there are no flashcards, print `There is no flashcard to practice!` and return to the main menu (1).

Your flashcard should appear on the screen in the following way:

```
Question: {your question}
Please press "y" to see the answer or press "n" to skip:
```

If `y` is entered, the program should output `Answer: {your answer}` and go to the next flashcard. If there are no flashcards to show, return to the main menu (1).

If `n` is entered, skip to the next flashcard. If there are no flashcards to show, return to the main menu (1).

Once the program has reached the end of a flashcard list, return to the main menu (1).

Please keep in mind the following:

- In case of the wrong input, output the following message: `{wrong key} is not an option`. Wait for the right input. 
- Your questions and answers must be non-empty values. Otherwise, wait for the input. 
- Don't forget about the goodbye message. Output `Bye!` every time a user exits the program.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example 1:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Brazil?
Answer:
> Brasilia

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Lebanon?
Answer:
> Beirut

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Brazil?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Brasilia

Question: What is the capital city of Lebanon?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Beirut

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Montenegro?
Answer:
> Podgorica

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Brazil?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Brasilia

Question: What is the capital city of Lebanon?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Montenegro?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Podgorica

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


**Example 2:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 5

5 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> we

we is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 3

3 is not an option

1. Add a new flashcard
2. Exit
> 0w

0w is not an option

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
>
Question:
> What is the capital city of Japan?
Answer:
>

Answer:
>

Answer:
> Tokyo

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```

## <br/>Stage 2:
### _Store the flashcards_
In the previous stage, we created our first flashcards. The downside is that they are lost every time you close the program. We need to find a way to store them. We can use an SQLite database for this purpose. This database consists of a single file and is easy to install. To process this type of database with Python rather than SQL, we need [Object Relational Mapper (ORM)](https://en.wikipedia.org/wiki/Object-relational_mapping). SQLAlchemy can translate the Python classes to tables in relational databases and convert the function calls to SQL statements automatically.

&nbsp;

When establishing a connection with the database, you should add a `check_same_thread=False` flag to the database name so that Hyperskill can test your project properly
```
engine = create_engine('sqlite:///<your database name.db>?check_same_thread=False')
```
After that, we need to create tables in the database so that the `declarative_base()` function can establish a base class. A base class stores a catalog of classes and mapped tables in the declarative system.
```
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```
Once the base class is declared, we can define any number of mapped classes inside. For now, we want to store the answers and questions in the database. To do that we need to define the following class:
```
from sqlalchemy import Column, Integer, String

class MyClass(Base):
    __tablename__ = 'my_table'

    id = Column(Integer, primary_key=True)
    first_column = Column(String)
    second_column = Column(String)
```
A class in declarative form must have a `__tablename__` attribute and at least one `Column` that constitutes a primary key.

We also need to call the `MetaData.create_all()` method to create the corresponding table in the database.
```
Base.metadata.create_all(engine)
```
Now, you should create a session. And, finally, you are ready to add a new object to the table:
```
new_data = MyClass(first_column='What is the capital city of India', second_column='New Delhi')
session.add(new_data)
session.commit()
```
The added data will be pending until we call the `commit()` method.

The `query(<mapped class name>)` method can help you access the table data.
```
result_list = session.query(MyClass).all()
```
This code snippet above includes the `all()` method that returns a list of all added objects.
```
print(result_list[0].question)  # What is the capital city of India
print(result_list[0].answer)    # New Delhi
print(result_list[0].id)        # 1
```

&nbsp;

In this stage, your program should implement the features from Stage 1 and do the following:

1. Create a database. Please, name it `flashcard`: this will ensure the proper work of the tests (even though the tests will not check the file with the database itself). 
2. Create a table in the database, name it `flashcard`. 
3. Store a question in each table row with an answer and an ID.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example 1:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Hungary?
Answer:
> Budapest

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Chile?
Answer:
> Santiago

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


**Example 2:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Hungary?
Please press "y" to see the answer or press 'n' to skip:
> y

Answer: Budapest

Question: What is the capital city of Chile?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Santiago

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of China?
Answer:
> Beijing

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Hungary?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Chile?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Santiago

Question: What is the capital city of China?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Beijing

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


**Example 3:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 5

5 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> ww

ww is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 0

0 is not an option

1. Add a new flashcard
2. Exit
> q3

q3 is not an option

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Switzerland?
Answer:
> Basel

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
>
Question:
> What is the capital city of Australia?
Answer:
>

Answer:
>

Answer:
> Canberra

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Hungary?
Please press "y" to see the answer or press "n" to skip:
> s

Please press "y" to see the answer or press "n" to skip:
> y

Answer: Budapest

Question: What is the capital city of Chile?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of China?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Swiss?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Basel

Question: what is the capital city of Australia?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Canberra

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


## <br/>Stage 3:
### _Update the flashcards_
Different Query object methods can give access to the table entries. The `all()` method returns a list of all table entries, `update({<mapped class attribute>:<new value>})` replaces the existing value with a new value, `delete()` deletes query results. Take a look at how some of the methods can be applied:
```
entries = session.query(Database).all()  # get all table entries
entry = entries[0]

# the following lines update the entry
entry.value = 10
session.commit()

# the following lines delete the entry
session.delete(entry)
session.commit()
```
There are also such useful methods as `get(<primary key value>)` that returns an entry based on the given primary key, and `filter(<criteria>)` that returns only those entries that match the given criteria.

&nbsp;

In this stage, we are going to add new features to our program. For example, we may need to edit or get rid of some flashcards.

&nbsp;

We need to add new features to the menu that comes up once a user entered the `Practice flashcards` key from the previous stage. Let's call it the practice menu (3):
```
press "y" to see the answer:
press "n" to skip:
press "u" to update:
```
As you can see, it still contains the `y` and `n` options. A user advances to another menu by entering `u`. Let's call it the update menu (4).
```
press "d" to delete the flashcard:
press "e" to edit the flashcard:
```
`d` deletes a flashcard, the `e` option offers a way to edit the current flashcard. First, we need to edit the question:
```
current question: 
please write a new question: 
```
Once the question has been edited, proceed to the answer:
```
current answer: 
please write a new answer:
```
If the user leaves the question or the answer field empty, keep the original question or answer value unchanged.

> Output the `<wrong key> is not an option` message in both practice (3) and update (4) menus when a user presses the wrong key. Other parts of the program should operate as in the previous stages.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example 1:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There are no flashcards to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> Korea's capital?
Answer:
> Seoul

1. Add a new flashcard
2. Exit
> 1

Question:
> Is London England's capital?
Answer:
> Yes

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital of Ecuador?
Answer:
> Quito

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: Korea's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Seoul

Question: Is London England's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Yes

Question: What is the capital of Ecuador?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Quito

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: Korea's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> u
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> e

current question: Korea's capital?
please write a new question:
> What is the capital of South Korea?

current answer: Seoul
please write a new answer:
> Seoul

Question: Is London England's capital?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> u
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> d

Question: What is the capital of Ecuador?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y
Answer: Quito

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


**Example 2:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of South Korea?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> r
r is not an option
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> 4
4 is not an option
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> u
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> 1
1 is not an option
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> s
s is not an option
press "d" to delete the flashcard:
press "e" to edit the flashcard:
> d

Question: What is the capital of Ecuador?:
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
> g

g is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


## <br/>Stage 4:
### _The Leitner system_
We know how to create flashcards, but it is not enough. At the beginning of the project, we mentioned a special technique that can help us with our task of creating a useful memorizing tool. Don't worry, we are about to take off and our flashcards will help. We are going to implement the **Leitner system** in our program. In short, it introduces the concept of spaced repetition proposed by Sebastian Leitner, a German scientist. Leitner's system suggests reviewing cards at increased intervals.

We can divide the memorization process into several parts. First, you create several boxes (usually from 3 to 5) that will store your flashcards. You mark each box with time periods that show how frequently the cards should be reviewed. For example, Box 1 will contain the most difficult cards, so they should be reviewed every day; Box 2 will have easier cards that you will check more rarely, every two days, and so on.

Next, you start learning and arranging the flashcards. You go through multiple Sessions. During Session 1, all your cards are in Box 1. You answer questions on these cards. If you are right, the card moves to Box 2 — that means that you don't need to repeat the information on the card so often. If your answer is wrong, your card stays in Box 1 — that means that you will see this card more frequently. When you reach Session 2, you answer questions on the cards both in Box 1 and Box 2. During Session 3, you study the cards in all three boxes. Again, every time you get a card wrong, you move it to Box 1. If you get the card right, you move it to the next box.

![sessions](https://ucarecdn.com/ba46efaa-d774-4174-bfc6-6397dc79ff0d/)

In this stage, there are three boxes, and if you give the correct answers to the cards in the third box, it means you've learned them, and you don't need those cards anymore, so you can remove them from the database.

If you want to read about this method in a little more detail, refer to the [MindEdge article](https://www.mindedge.com/learning-science/the-leitner-system-how-does-it-work/). 

&nbsp;

After displaying each question, you need to ask users whether their answers are correct or not. To do this we need to create another menu, let's call it the learning menu (5):
```
press "y" if your answer is correct:
press "n" if your answer is wrong:
```
This will correspond to Session 1 for these cards. New flashcards and cards with wrong answers should go to the first box. Once you reach Session 3 for them, you can remove them from the database.

A good idea would be to add a column that will stand for the "box number". When a new flashcard is created, set it to some value, and update it once the user answers the card correctly during practicing.

> Output the `<wrong key> is not an option` message when a user presses the wrong key. Other parts of the program should operate as in the previous stages.

The skipped questions remain in the same boxes. Do not display a learning menu (5) for them.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example 1:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2
There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1
1. Add a new flashcard
2. Exit
> 1

Question:
> What is the Capital of Turkey?
Answer:
> Ankara

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital of Croatia?
Answer:
> Zagreb

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2
There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```


**Example 2:**
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 6
6 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1
1. Add a new flashcard
2. Exit
> 3
3 is not  an option

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
> what is the capital of Iran?
Answer:
> Tehran

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: what is the capital of Iran?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> 6
6 is not an option

press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Tehran
press "y" if your answer is correct:
press "n" if your answer is wrong:
>>
 is not an option

press "y" if your answer is correct:
press "n" if your answer is wrong:
>> b
b is not an option

press "y" if your answer is correct:
press "n" if your answer is wrong:
>> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```
