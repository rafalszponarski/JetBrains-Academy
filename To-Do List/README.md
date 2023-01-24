# Steps needed to complete project "[**_To-Do List_**](https://hyperskill.org/projects/105)"

## <br/>Stage 1:
### _Plan it!_
Do you have 10 minutes a day to add an extra $4000 to your monthly income?

This is the difference between people who write down their goals and those who don’t. That’s one of many reasons why having a To-Do list can improve your work and personal life. You can use it to reduce stress in your life and be more productive. It also helps you become more persistent and save time for the best things in your life.

In this project, you will create a to-do list that will help you organize your life.

&nbsp;

To begin with, develop a simple list that contains four tasks. Your program must print the list in the example.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example:** a list for your program
```
Today:
1) Do yoga
2) Make a breakfast
3) Learn the basics of SQL
4) Learn about ORM
```

## <br/>Stage 2:
### _Accumulate it!_
It's not good that when you close the to-do list application, the tasks disappear. To avoid this, you need to create a database where you can store all information about your tasks. We will use SQLite to create a database and SQLAlchemy to manage the database from Python.

First, you need to create a database file. To create it, use the `create_engine()` method, where `file_name` is the database file name:

```
from sqlalchemy import create_engine

engine = create_engine('sqlite:///file_name?check_same_thread=False')
```

The `check_same_thread=False` argument connects a database from another thread. Please, set it as described, as the tests require it. Otherwise, you will get an exception.

Once you've created your database file, you need to create a table inside. First, create a **model class** that describes the table in the database. Consider a piece of code below when doing it:

```
class Table(Base):
    ...
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field
```

- `String_field` is a string column; `default='default_value'` indicates that the default value of this column is `default_value`; 
- `Date_field` is a column that stores the date. SQLAlchemy automatically converts the SQL `date` into a Python `datetime` object; 
- The `__repr__` method returns a string representation of the class object. In the ORM concept, each row in the table is an object of a class.


Once you are done with the table description, you need to add it to the database. This will create a table in the database by generating SQL queries according to the described models. Now, we can access the database. To do this, create a session.

The `session` object is the only thing you need to manage the database. This is how you can create a new row in the table:

```
new_row = Table(string_field='This is a string field!',
         date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
```

To get all rows from the table, you can pass the model class to the `query()` method that selects all rows from the table represented by a model class:

```
rows = session.query(Table).all()
```

The `all()` method returns all rows from the table as a Python list. Each element of this list is an object of the model class. You can access the row fields by their names:

```
first_row = rows[0] # In case rows list is not empty

print(first_row.string_field) # Will print the value of the string_field
print(first_row.id) # Will print the id of the row
print(first_row) # Will print the string that was returned by the __repr__ method
```

&nbsp;

To complete this stage, you need to arrange the data storage in the database. Here's what you need to do:

1. Create a database file. Name it as `todo.db`;
2. Create a table in this database. Name it as `task`.

The table `task` should have the following columns:

- An integer column named `id`. Arrange it as the `primary key`; 
- A string column named `task`; 
- A date column named `deadline`. It should have the date when the task was created by default. You can use the `datetime.today()` method.

Also, you need to implement a menu that will make your program more convenient. The menu should have the following items:

1. `Today's tasks`. It prints all the tasks for today; 
2. `Add a task`. It asks for task descriptions and saves them in the database; 
3. `Exit`.


&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example:** an example of the program output
```
1) Today's tasks
2) Add a task
0) Exit
> 1

Today:
Nothing to do!

1) Today's tasks
2) Add a task
0) Exit
> 2

Enter a task
> Prepare a presentation
The task has been added!

1) Today's tasks
2) Add a task
0) Exit
> 1

Today:
1. Prepare a presentation

1) Today's tasks
2) Add a task
0) Exit
> 0

Bye!
```

## <br/>Stage 3:
### _Deadlines are scary, aren't they?_
Every day we’re surrounded by thousands of small distractions, facts, and bits of odd information. When you’re facing a deadline, you don’t have time for all this fluff. You need to focus on the task at hand. You can’t afford to spend hours on Pinterest, chatting with your coworkers, or watching re-runs on TV.

Let's add the ability to set the deadlines for our tasks. For this, we need to use the Python datetime module. Here are some methods that can help you:

from `datetime` import datetime, timedelta

```
datetime.today() # returns the current date and time
datetime.today().date() # the current date without time
datetime.today().time() # the current time without date

datetime.strptime(date_string, format) # returns a datetime corresponding to the date_string, parsed according to format.
# Format example: '%Y-%m-%d' - '2020-04-24'

today = datetime.today()
today.day # today's day
today.strftime('%b') # the short name of the current month, for example, Apr
today.weekday() # returns the day of the week as an integer; Monday is 0 and Sunday is 6.

yesterday = today - timedelta(days=1) # a timedelta object that represents a duration, the difference between two dates or times.
day_after_tomorrow = today + timedelta(days=2)
```

To select the rows based on a certain condition, use the `filter()` method that accepts a condition:

```
from datetime import datetime

today = datetime.today()
rows = session.query(Table).filter(Table.date == today.date()).all()
```

In the code snippet above, we have selected all rows from `Table` where the date column is today's date. To sort the selected data, you can use `order_by()` that accepts a sorting column:

```
# select all rows ordered by the date column
session.query(Table).order_by(Table.date).all()

# select all rows where string_fields starts with 'L'. The result is ordered by the date column
session.query(Table).filter(Table.string_field.startswith('L'))).order_by(Table.date).all()
```

&nbsp;

Add the following items to your menu:

1. `Week's tasks`. It prints all tasks for the next 7 days from today; 
2. `All tasks`. It prints all tasks sorted by the deadline; 
3. The `Add a task` item should ask for the deadline of the task. Users need to input the deadline in the following format: `YYYY-MM-DD`; 
4. The `Today's tasks` item should also print today's date (refer to the Example section for the format).

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example:** possible output of your program
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task 
0) Exit
> 1

Today 26 Apr:
Nothing to do!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task 
0) Exit
> 4

Enter a task 
> Meet my friends
Enter a deadline 
> 2020-04-28
The task has been added!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task 
0) Exit
> 2

Sunday 26 Apr:
Nothing to do!

Monday 27 Apr:
Nothing to do!

Tuesday 28 Apr:
1. Meet my friends

Wednesday 29 Apr:
Nothing to do!

Thursday 30 Apr:
1. Math homework
2. Call my mom

Friday 1 May:
1. Order a new keyboard

Saturday 2 May:
Nothing to do!
> 3

All tasks:
1. Meet my friends. 28 Apr
2. Math homework. 30 Apr
3. Call my mom. 30 Apr
4. Order a new keyboard. 1 May

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task 
0) Exit
> 0

Bye!

Bye!
```

## <br/>Stage 4:
### _Bye-bye, completed tasks_
Planning is one thing, but when we need to knuckle down and put our plans into action, we tend to push our tasks back until the very last minute. Or even worse, we often tend to miss the established deadline. It happens even to the best of us! In this stage, let's implement the ability to see the tasks with a missed deadline and delete them.

To delete a row from the table, use the `delete()` method that accepts an object. As you remember, each row is represented by a Python object:

```
from datetime import datetime

# delete all rows where the date column is today's date
session.query(Table).filter(Table.date == datetime.today().date()).delete()

# delete a specific row
rows = session.query(Table).filter(Table.date < datetime.today().date()).all()
specific_row = rows[0] # in case rows is not empty
session.delete(specific_row)

# don't forget to commit the changes
session.commit()
```

&nbsp;

Add the following items to your menu:

1. `Missed tasks`. It prints all the tasks with a missed deadline. Order the tasks by the deadline date; 
2. `Delete a task`. It deletes the chosen task. Print `Nothing to delete` if the tasks list is empty. This menu should also print all the tasks sorted by the deadline date and ask to enter the number for the task.

See the Example section for further detail.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Notice that it's not the part of the input.

**Example:** possible output of the program
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task 
6) Delete a task 
0) Exit
> 4

Missed tasks:
1. Learn the for-loop. 19 Apr

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task 
6) Delete a task 
0) Exit
> 6

Choose the number of the task you want to delete:
1. Learn the for-loop. 19 Apr
2. Learn the basics of SQL. 29 Apr
> 1
The task has been deleted!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task 
6) Delete a task 
0) Exit
> 4

Missed tasks:
All tasks have been completed! 

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task
6) Delete a task
0) Exit
> 0

Bye!
```
