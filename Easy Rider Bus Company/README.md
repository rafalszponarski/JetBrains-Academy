# Steps needed to complete project "[**_Easy Rider Bus Company_**](https://hyperskill.org/projects/128)"

## <br/>Stage 1:
### _Checking the data type_
You just started sorting out the existing database of the "Easy Rider" bus company. As you take the first look at the data, you realize that it's not going to be easy.

Sometimes numbers are missing from where they should definitely be. You also noticed that sometimes there are too many or too few characters. Fortunately, there is documentation to help you sort out this mess. However, this documentation is not a hundred percent complete: part of it was torn away when your colleague spilled coffee on it. Let's see what we can make out.

Here are the documents that you have: [documentation](https://stepik.org/media/attachments/lesson/412967/Documentation.jpg) and [diagram of the bus lines](https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg).

&nbsp;

1. The string containing the data in JSON format is passed to standard input. 
2. Check that the data types match. 
3. Check that the required fields are filled in. 
4. Display the information about the number of found errors in total and in each field. Keep in mind that there might be no errors at all. 
5. The output should have the same formatting as shown in the example.

> No need to worry about the format (name validation) now. Let's at first just make sure that the fields have the right type and all required ones are filled.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the type `Char` is present among the data types. 

&nbsp;

**Example:**
Input:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": 8.12
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": "7",
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": "",
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": ""
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": "0",
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": "512",
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": 5,
        "a_time": "08:16"
    }
]
```
Output:
```
Type and required field validation: 8 errors
bus_id: 2
stop_id: 1
stop_name: 1
next_stop: 1
stop_type: 1
a_time: 2
```


## <br/>Stage 2:
### _Correct syntax_
You managed to fill in all the missing data and correct the mistakes with the types. However, you noticed that there are multiple problems with suffix names for the stops: sometimes they are incorrect, and sometimes they are simply missing. As if that was not enough, you also realized that there are errors in the arrival times.

It seems like you have to carefully look at the entire "Format" column in the first part of the documentation.

Here are the documents that you have: [documentation](https://stepik.org/media/attachments/lesson/412967/Documentation.jpg) and [diagram of the bus lines](https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg).

&nbsp;

1. The string containing the data in JSON format is passed to standard input. 
2. Check that the data format complies with the documentation. 
3. Only the fields that have such a requirement are relevant, i.e. `stop_name`, `stop_type`, `a_time`, so, please, count errors only for them. 
4. Like in the previous stage, print the information about the number of found errors in total and in each field. Remember that there might be no errors at all. 
5. The output should have the same formatting as shown in the example.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation.

Note that the time format is military time (24 hours, `hh:mm`). That means that there are certain restrictions:

- the first digit cannot be 3, 4, etc.; 
- hours less than 10 should have zero in front of them, e.g. `08:34`; 
- the delimiter should be colon `:`.

&nbsp;

**Example:**
Input:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Av.",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "8:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "OO",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:77"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "A",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10.12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "bourbon street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "38:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output:
```
Format validation: 9 errors
stop_name: 3
stop_type: 2
a_time: 4
```


## <br/>Stage 3:
### _Bus line info_
It wasn't easy, but finally, you verified the data format and the required fields. It is now time to check how many bus lines we have and how many stops there are on each line. Before we can go further with sorting out the database, it would be a good idea to check that the information is complete.
Here are the documents that you have: [documentation](https://stepik.org/media/attachments/lesson/412967/Documentation.jpg) and [diagram of the bus lines](https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg).

&nbsp;

1. The string containing the data in JSON format is passed to standard input. 
2. Find the names of all the bus lines. 
3. Verify the number of stops for each line. 
4. The output should have the same formatting as shown in the example.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation

&nbsp;

**Example:**
Input:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output:
```
Line names and number of stops:
bus_id: 128, stops: 4
bus_id: 256, stops: 4
bus_id: 512, stops: 2
```

## <br/>Stage 4:
### _Special stops_
The missing part of the specification is nowhere to be found. You need to recover and update the data contained in the second part of the documentation.

The company is growing, the number of bus lines is ever-increasing, and logically, more bus stops appear. You need to prepare an appropriate function that calculates this data so that it doesn't have to be checked manually in the future.
Here are the documents that you have: [documentation](https://stepik.org/media/attachments/lesson/412967/Documentation.jpg) and [diagram of the bus lines](https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg).

&nbsp;

1. The string containing the data in JSON format is passed to standard input. 
2. Make sure each bus line has exactly one starting point (`S`) and one final stop (`F`). 
3. If a bus line does not meet this condition, stop checking and print a message about it. Do not continue checking the other bus lines. 
4. If all bus lines meet the condition, count how many starting points and final stops there are. Print their unique names in alphabetical order. 
5. Count the transfer stops and print their unique names in alphabetical order. A transfer stop is a stop shared by at least two bus lines. 
6. The output should have the same formatting as shown in the example.

If you cannot find the necessary information in the stage description, it can probably be found in the attached documentation

&nbsp;

**Example 1:**
Input 1:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output 1:
```
There is no start or end stop for the line: 512.
```

**Example 2:**
Input 2:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output 2:
```
Start stops: 3 ['Bourbon Street', 'Pilotow Street', 'Prospekt Avenue']
Transfer stops: 3 ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
Finish stops: 2 ['Sesame Street', 'Sunset Boulevard']
```


## <br/>Stage 5:
### _Unlost in time_
It is now time to move on to a more detailed analysis. First, check that arrival times for the upcoming stops make sense: they are supposed to be increasing, that is, going forward in time. After all, there is no information in the documentation that your company offers time travel
Here are the documents that you have: [documentation](https://stepik.org/media/attachments/lesson/412967/Documentation.jpg) and [diagram of the bus lines](https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg).

&nbsp;

1. The string containing the data in JSON format is passed to standard input. 
2. Check that the arrival time for the upcoming stops for a given bus line is increasing. 
3. If the arrival time for the next stop is earlier than or equal to the time of the current stop, stop checking that bus line and remember the name of the incorrect stop. 
4. Display the information for those bus lines that have time anomalies. For the correct stops, do not display anything. 
5. If all the lines are correct timewise, print `OK`. 
6. The output should have the same formatting as shown in the example.

If you can't find the necessary information in the stage description, it can probably be found in the attached documentation

&nbsp;

**Example 1:**
Input 1:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:17"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:07"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:44"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output 1:
```
Arrival time test:
bus_id line 128: wrong time on station Fifth Avenue
bus_id line 256: wrong time on station Sunset Boulevard
```

**Example 2:**
Input 2:
```
[
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output 2:
```
Arrival time test:
OK
```


## <br/>Stage 6:
### _On-demand_
The work seemed tedious and endless, but it finally looks like we're getting there. There is only one more point left in the specification that we need to check and fix: on-demand stops cannot be initial, final, or transfer stops.
Here are the documents that you have: [documentation](https://stepik.org/media/attachments/lesson/412967/Documentation.jpg) and [diagram of the bus lines](https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg).

&nbsp;

1. The string containing the data in JSON format is passed to standard input. 
2. Check that all the departure points, final stops, and transfer stations are not "On-demand". 
3. Display the unique names of the stops containing this type of issue. Sort them in ascending order. 
4. If everything is fine, print `OK`. 
5. The output should have the same formatting as shown in the example.

If you cannot find the necessary information in the stage description, it can probably be found in the attached documentation.

&nbsp;

**Example 1:**
Input 1:
```
[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "O",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output 1:
```
On demand stops test:
Wrong stop type: ['Elm Street', 'Sunset Boulevard']
```


**Example 2:**
Input 2:
```
[
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]
```
Output 2:
```
On demand stops test:
OK
```
