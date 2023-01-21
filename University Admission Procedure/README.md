# Steps needed to complete project "[**_University Admission Procedure_**](https://hyperskill.org/projects/163)"

## <br/>Stage 1:
### _No one is left behind!_
Let's create a program that will help the university determine the best candidates for enrolling!

The first step is very simple. An applicant needs to take three exams and submit the scores. The score of an exam can vary from 0 to 100. Your program should read the numbers representing the exam scores, calculate the mean exam score, and output it. Finally, enroll the applicant to the university, as there are no other contestants yet.

&nbsp;

At this stage, your program should:

1. Take three inputs as integer numbers. They are the exam results. 
2. Calculate the mean score of all three numbers. If the mean is a fractional number, don't discard the fractional part. 
3. Print the resulting number. 
4. Print the `Congratulations, you are accepted!` line.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example**
```
> 75
> 90
> 68
77.66666666666667
Congratulations, you are accepted!
```


## <br/>Stage 2:
### _Raising the bar_
It'd be great if universities could enroll everybody, but it's not very realistic, is it? Let's refine our algorithm. In this stage, we need to set a threshold of the mean score — if the mean score of the applicant is equal to or greater than `60.0`, the program should notify the applicant of their acceptance to the university. Otherwise, inform them about their rejection.

&nbsp;

At this stage, your program should:

1. Read the numbers and output the mean score, as in the previous stage. 
2. If the mean score is equal to or greater than `60.0`, output the following message: `Congratulations, you are accepted!` 
3. If the mean score is less than `60.0`, output the following message: `We regret to inform you that we will not be able to offer you admission.`

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** the applicant is enrolled
```
> 70
> 56
> 81
69.0
Congratulations, you are accepted!
```


**Example 2:** the applicant is rejected
```
> 100
> 43
> 27
56.666666666666664
We regret to inform you that we will not be able to offer you admission.
```


## <br/>Stage 3:
### _Going big_
Things are heating up! Our university has become trendy, so the applicants are rushing in. Your program has to be adapted to this — unfortunately, we cannot enroll everybody. The program will need to rank the potential students and determine who's going to get admitted. At this stage, you'll need to work with the Grade Point Average (GPA). It is the mean grade of all high school courses. We don't need the threshold, for now, a certain number of applicants with the best GPA will be accepted instead.

&nbsp;

To proceed further we need to understand the basics of sorting. To use more than one attribute for list sorting, use the following syntax:
```
not_sorted_list = [['c', 11], ['a', 11], ['c', 10]]
sorted_list = sorted(not_sorted_list, key=lambda x: (x[0], x[1]))
print(sorted_list)
# [['a', 11], ['c', 10], ['c', 11]]
```

In this example, the first value (`x[0]`) of each element of the `not_sorted_list` is used for sorting in the first place. If these values are equal, the second value (`x[1]`) is used to determine which element is greater.

A problem may occur if you want to sort the list in ascending order by the first value and in descending order by the second value. For example, you have two values to sort the list by: score and time.
```
# the first element in each nested list is score
# the second element is time
not_sorted_list = [[531, 11.76], [401, 5.11], [531, 10.05]]
```

You want to sort your list in such a way that the elements with the highest score and the smallest time value would go before the elements with a lower score and greater time value. To do this, you can simply inverse one of the values by adding a minus in front of it:

```
# both lines will lead to the same result
sorted_list = sorted(not_sorted_list, key=lambda x: (-x[0], x[1]))
sorted_list = sorted(not_sorted_list, reverse=True, key=lambda x: (x[0], -x[1]))
print(sorted_list)
# [[531, 10.05], [531, 11.76], [401, 5.11]]
```

&nbsp;

At this stage, your program should:

1. Read the first input, an **N** integer representing the total number of applicants. 
2. Read the second input, an **M** integer representing the number of applicants that should be accepted to the university. 
3. Read N lines from the input. Each line contains the first name, the last name, and the applicant's GPA. These values are separated by one whitespace character. A GPA is a floating-point number with two decimals. 
4. Output the `Successful applicants:` message. 
5. Output M lines for applicants with the top-ranking GPAs. Each line should contain the first and the last name of the applicant separated by a whitespace character. Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on. 
6. If two applicants have the same GPA, rank them in alphabetical order using their full names (we know it's not really fair to choose students by their names, but what choice do we have?)

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> 5
> 3
> Cole Collins 3.68
> Dolores Baldwin 3.40
> Brett Boyer 2.45
> Nora Alston 3.71
> Jessy Moore 3.14
Successful applicants:
Nora Alston
Cole Collins
Dolores Baldwin
```

**Example 2:**
```
> 3
> 2
> Albert Collins 3.02
> Albert Nelson 3.02
> Cole Allen 3.02
Successful applicants:
Albert Collins
Albert Nelson
```


## <br/>Stage 4:
### _Choose your path_
Good news everyone: our university keeps growing larger! Five departments have been established; now our potential students can apply to the Mathematics, Physics, Biotech, Chemistry, or the Engineering Department. Each applicant needs to choose three departments and rank them. First, the department with the highest priority; second, the department in case the first option doesn't work out. The third department is Plan C.

Your task for this stage is to develop an algorithm that will sort the applicants according to their GPA and take into account their priorities: if the applicant doesn't score high enough to get accepted to the department of first priority, they'll participate in the rankings for the second priority, and so on.

In other words, the admission algorithm should work by the following rules:

1. Firstly, the ranking list for every department is created according to the applicant's first priorities. People who chose Physics as their first priority only participate in ranking for the Physics department, and so on. 
2. Applicants are scored according to their GPA. People who have a higher GPA score are ranked higher in the department's ranking list. 
3. Each department accepts N (maximum number of students for the department) best students from the department's ranking list. If there are fewer than N students on the department's list, all students from the list are accepted. 
4. The accepted students are removed from the general list of applicants and no longer participate in the ranking. 
5. The same procedure is repeated for the second priorities. If there are departments that accepted fewer than N students in the first stage of admission, these departments try to accept more students to fill all N student positions. 
6. The same procedure is repeated for the third priority.

The number of applicants is increasing, so instead of parsing the data through manual input, we've created [the file](https://stepik.org/media/attachments/lesson/493610/applicant_list.txt) that contains the list of potential students for your program to read. It is much more convenient to provide your program with information on applicants in this way.

&nbsp;

In this stage, your program should:

1. Read an **N** integer from the input. This integer represents the maximum number of students for each department. 
2. Read [the file](https://stepik.org/media/attachments/lesson/493610/applicant_list.txt) named applicants.txt (this file is already included in the project's files, even though it is not visible; so you only need to download it if you want to take a closer look at it). Each line equals one applicant, their first name, last name, GPA, first priority department, second priority department, and third priority department. Columns with values are separated by whitespace characters. For example, `Laura Spungen 3.71 Physics Engineering Mathematics`. 
3. Sort applicants according to their GPA and priorities (and names, if their GPA scores are the same). As in the previous stage, if two applicants to the same department have the same GPA, sort them by their full names in alphabetical order. 
4. For each department, choose the **N** best candidates. Some departments are less popular than others, so there may be fewer available candidates for a department. However, their number shouldn't be more than **N**. 
5. Print the departments in the alphabetic order (Biotech, Chemistry, Engineering, Mathematics, Physics), output the names and the GPA of enrolled applicants for each department. Separate the name and the GPA with a whitespace character. Here's an example (you may add empty lines between the departments' lists to increase the text readability):

```
department_name
applicant1 GPA1
applicant2 GPA2
applicant3 GPA3
<...>
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:** There are enough students for all departments
Below is an example of the input file:
```
Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
```

An example of the output:
```
> 4
Biotech
Randon Bradhust 3.68
Narissa Worthington 3.3
Natha Keefe 3.14
Cynthia Hermitton 3.1

Chemistry
Crescentia Dow 3.79
Halima Brydone 3.72
Estephanie Phelps 3.21
Tawny Crockett 3.01

Engineering
Tommi Peerless 3.85
Cheyla Hankinson 3.82
Nicolasa Sumpter 3.82
Lorry Bunger 3.79

Mathematics
Dashawn Bosley 3.54
Aundria Guthrie 3.51
Kennon Inverarity 3.5
Teneil Maclean 3.22

Physics
Darrah Smyth 3.89
Giovanna Keel 3.25
Cressie Gillespie 3.1
Fatemah Desavigny 3.0
```


**Example 2:** There aren't enough students for all departments:
The same textfile:
```
Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
```

An example of the output:
```
> 8
Biotech
Randon Bradhust 3.68
Narissa Worthington 3.3

Chemistry
Crescentia Dow 3.79
Halima Brydone 3.72
Estephanie Phelps 3.21
Tawny Crockett 3.01

Engineering
Tommi Peerless 3.85
Cheyla Hankinson 3.82
Nicolasa Sumpter 3.82
Lorry Bunger 3.79
Natha Keefe 3.14
Cynthia Hermitton 3.1
Marti Mclaws 3.05

Mathematics
Dashawn Bosley 3.54
Aundria Guthrie 3.51
Kennon Inverarity 3.5
Teneil Maclean 3.22
Shealynn Melville 3.02
Esther Bratby 2.67

Physics
Darrah Smyth 3.89
Giovanna Keel 3.25
Cressie Gillespie 3.1
Fatemah Desavigny 3.0
```


## <br/>Stage 5:
### _Special knowledge_
Taking only student's GPAs into consideration may not be very conclusive. It would be better if we could take the results of the finals depending on the Department. For example, for a Physics department candidate, we would check the physics finals. Try to take the sorting algorithm to the next level. In this stage, you need to sort by an exam that suits the particular Department.

&nbsp;

At this stage, your program should:

1. Read an **N** integer. This integer represents the maximum number of students for each department. 
2. Read [the file](https://stepik.org/media/attachments/lesson/493610/applicant_list_5.txt) named applicants.txt once again. The structure has changed a bit: instead of the GPA column, each line contains four columns with scores for particular exams: physics, chemistry, math, computer science (in this order). For example, `John Ritchie 89 45 83 75 Physics Engineering Mathematics`. 
3. Take into account the following exam results for the departments: physics for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science for the Engineering, and chemistry (again) for the Biotech department. 
4. Do the same steps as in the previous stage: perform three stages of admission based on the applicants' priorities. Applicants should be ranked by their exam score and, in case they have the same score, their full name in alphabetic order. There should be no more than N accepted applicants for each department. One student can only be accepted to one department. 
5. One thing has changed — output the exam result (instead of the GPA) for each student:

```
department_name
applicant1 exam1
applicant2 exam2
applicant3 exam3
<...>
```

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example**
Below is an example of the input file:
```
Natha Keefe 71 67 53 60 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 Physics Biotech Engineering
```

This is an example of the output:
```
> 5
Biotech
Randon Bradhust 88.0
Marti Mclaws 71.0
Narissa Worthington 71.0
Natha Keefe 67.0

Chemistry
Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
Dashawn Bosley 79.0

Engineering
Lorry Bunger 97.0
Tommi Peerless 92.0
Cheyla Hankinson 88.0
Cynthia Hermitton 88.0
Nicolasa Sumpter 81.0

Mathematics
Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0

Physics
Cressie Gillespie 85.0
Giovanna Keel 84.0
Fatemah Desavigny 81.0
Darrah Smyth 75.0
```


## <br/>Stage 6:
### _Extensive training_
Some of the departments proposed an improvement to the algorithm. They need more than one exam result for each applicant. For example, the Physics Department needs both math and physics exams, while the Mathematics Department is satisfied with the math exam only. Let's implement this request to make our departments happy (the applicants on the other hand...)

&nbsp;

In this stage, your program should:

1. Read an **N** integer from the input. This integer represents the maximum number of students for each department. 
2. Read [the file](https://stepik.org/media/attachments/lesson/493610/applicant_list_6.txt) named applicants.txt once again. The file has the same structure as in the previous stage. 
3. Consider the following exam results for departments: physics and math for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department. 
4. As in the previous stage, the exams are listed in the following order for each applicant: physics, chemistry, math, computer science. 
5. For the departments that need several exams, calculate the mean score and use it to rank the applicants (use floating-point numbers with at least one decimal). Otherwise, use the result for a single exam. 
6. Keep the rest of the steps the same as in the previous stage (once again, there should be no more than N accepted applicants for each department; use the same principles for sorting). 
7. Instead of printing the results (you may do it if you want), output the admission lists to files. Create a file for each department, name it %department_name%.txt, for example, physics.txt. Write the names of the students accepted to the department and their mean finals score to the corresponding file (one student per line).

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example**
Below is an extract of the input file:
```
Natha Keefe 71 67 53 60 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 Physics Biotech Engineering
```

The terminal output:
```
> 7
```

The examples of the output to different files:

biotech.txt:
```
Randon Bradhust 80.0
Narissa Worthington 61.5
```

chemistry.txt:
```
Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
```

engineering.txt:
```
Lorry Bunger 90.5
Nicolasa Sumpter 88.5
Cheyla Hankinson 87.0
Tommi Peerless 86.5
Cynthia Hermitton 75.0
Marti Mclaws 60.5
Natha Keefe 56.5
```

mathematics.txt:
```
Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0
Dashawn Bosley 82.0
```

physics.txt:
```
Cressie Gillespie 83.5
Giovanna Keel 80.0
Darrah Smyth 79.5
Fatemah Desavigny 77.0
```


## <br/>Stage 7:
### _Something special_
It seems like our potential students are upset because of the last change in our algorithm. Instead of passing one exam, many of them need to worry about passing two exams with good scores. We are ready to give them a second chance. Now they can try to pass a special university admission exam! If the candidate's score on this exam is better than their mean score for the finals required by a Department, the university is ready to discard the results of the finals.

&nbsp;

At this stage, your program should:

1. Read an **N** integer from the input. This integer represents the maximum number of students for each department. 
2. Read [the file](https://stepik.org/media/attachments/lesson/493610/applicant_list_7.txt) named applicants.txt once again. Mind one additional column, right after the last exam's result. This column represents the special exam's score. For example, `Willie McBride 76 45 79 80 100 Physics Engineering Mathematics`(where 100 is the admission exam's score). 
3. Choose the best score for a student in the ranking: either the mean score for the final exam(s) or the special exam's score. Use the same set of finals for each Department as in the previous stage. Note that you may need to compare the values several times: for example, if a student doesn't get accepted to the Department of the first priority, compare the finals mean score and the special exam's score once again (but this time, for the second priority department). 
4. Keep the rest of the steps the same as in the previous stage. Once again, there should be no more than **N** accepted applicants for each department; use the same principles for sorting. 
5. Output the names and the student's best score, either the mean finals score or the special exam's score to the files.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example**
Below is an extract of the input file:
```
Natha Keefe 71 67 53 60 31 Engineering Biotech Chemistry
Crescentia Dow 86 94 85 51 80 Chemistry Physics Mathematics
Randon Bradhust 72 88 85 83 59 Biotech Engineering Chemistry
Dashawn Bosley 80 79 82 61 40 Mathematics Chemistry Biotech
Nicolasa Sumpter 75 82 96 81 38 Engineering Mathematics Biotech
Cressie Gillespie 85 92 82 70 59 Physics Mathematics Engineering
Tawny Crockett 71 90 80 72 44 Chemistry Biotech Physics
Kennon Inverarity 71 84 98 71 72 Mathematics Engineering Chemistry
Halima Brydone 77 85 82 86 50 Chemistry Physics Mathematics
Esther Bratby 55 76 88 62 30 Mathematics Chemistry Biotech
Lorry Bunger 75 73 84 97 22 Engineering Biotech Physics
Fatemah Desavigny 81 71 73 86 78 Physics Mathematics Engineering
Marti Mclaws 71 71 61 60 41 Engineering Chemistry Biotech
Estephanie Phelps 80 95 45 71 80 Chemistry Physics Mathematics
Tommi Peerless 72 81 81 92 75 Engineering Physics Mathematics
Cynthia Hermitton 70 59 62 88 80 Engineering Biotech Chemistry
Cheyla Hankinson 75 80 86 88 36 Engineering Mathematics Biotech
Giovanna Keel 84 71 76 80 79 Physics Mathematics Engineering
Narissa Worthington 52 71 80 73 81 Biotech Chemistry Mathematics
Aundria Guthrie 61 81 94 71 21 Mathematics Chemistry Engineering
Teneil Maclean 85 63 84 45 69 Mathematics Physics Chemistry
Shealynn Melville 74 76 88 62 70 Mathematics Chemistry Physics
Darrah Smyth 75 73 84 97 94 Physics Biotech Engineering
```

The terminal output:
```
> 7
```

The examples of the output to different files:

biotech.txt:
```
Narissa Worthington 81.0
Randon Bradhust 80.0
```

chemistry.txt:
```
Estephanie Phelps 95.0
Crescentia Dow 94.0
Tawny Crockett 90.0
Halima Brydone 85.0
```

engineering.txt:
```
Lorry Bunger 90.5
Nicolasa Sumpter 88.5
Cheyla Hankinson 87.0
Tommi Peerless 86.5
Cynthia Hermitton 80.0
Marti Mclaws 60.5
Natha Keefe 56.5
```

mathematics.txt:
```
Kennon Inverarity 98.0
Aundria Guthrie 94.0
Esther Bratby 88.0
Shealynn Melville 88.0
Teneil Maclean 84.0
Dashawn Bosley 82.0
```

physics.txt:
```
Darrah Smyth 94.0
Cressie Gillespie 83.5
Giovanna Keel 80.0
Fatemah Desavigny 78.0
```
