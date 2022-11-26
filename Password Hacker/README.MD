# Steps needed to complete project "[**_Password Hacker_**](https://hyperskill.org/projects/80)"

## <br/>Stage 1:
### _Establishing a connection_
Imagine some admin who runs a website on the Internet. The site is becoming very popular, and a lot of people register. Filling in their profiles, they leave some information there that is not meant to be public, for example, information about their credit cards.

The admin completely forgot about the security of the site, so now you can log in with admin privileges without even having a login and password!

The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site. It will get harder: the tasks of all other stages of the project will be to crack the admin password. Good luck!

Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.


<br/>Your program will receive command line arguments in this order:

1. IP address
2. port
3. message for sending

The algorithm is the following:

1. Create a new socket.
2. Connect to a host and a port using the socket. 
3. Send a message from the third command line argument to the host using the socket. 
4. Receive the server’s response. 
5. Print the server’s response. 
6. Close the socket.


<br/>The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> python hack.py localhost 9090 password
Wrong password!
```

**Example 2:**
```
> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
```


## <br/>Stage 2:
### _Simple brute force_
The admin noticed someone sneaking around the site with admin rights and came up with a password. Now to log in as an admin, you need to enter the password first. Maybe the admin has set a relatively easy and short password so that it is easy to remember? Let's try to brute force all possible passwords to enter the site!

So far the program is very simplistic: it’s time to improve it so that it can generate different variants of the password and then try each one. The admin of the server doesn’t hide the information that passwords vary in length and may include letters from `a` to `z` and numbers from `0` to `9`. You should start with `a,b,c,....,z,0,1,..aa,ab,ac,ad` and continue until your password is correct. The `itertools.product()` function can help you here. It’s very important to try all the variants of every length because otherwise your program risks never finding the password!

If the password is correct, you will receive the `Connection success!` message. Otherwise, you will see the `Wrong password!` message. The server cannot receive more than a million attempts, so if your program works indefinitely, you will see the unfortunate message `Too many attempts`.


<br/>In this stage, you should write a program that:

1. Parses the command line and gets two arguments that are IP address and port.
2. Tries different passwords until it finds the correct one.
3. Prints the password it found.

Note that you can connect to the server only once and then send messages many times. Don't connect to the server before sending every message.

Also, note that here and throughout the project, the password is different every time you check your code.


<br/>The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

**Example:**
```
> python hack.py localhost 9090
pass
```



## <br/>Stage 3:
### _Smarter, dictionary-based brute force_
Looks like you can already call yourself a hacker! However, the situation gets more complicated: the admin improves the server and our simple brute force attack is no longer working. Well, this shouldn't hold you back: you can provide your program with a prepared [dictionary of typical passwords](https://stepik.org/media/attachments/lesson/255258/passwords.txt) (it was generated using a [database with over a million real-life passwords](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/)).

That's not all: the admin decided to outsmart us and changed the case of some letters in the new password so that we could not crack it using the password dictionary. Let's outsmart the admin and try all possible combinations of upper and lower case for each letter for all words of the password dictionary. We won't have to try too much since for a 6-letter word you'll get only 64 possible combinations.

Now you need not only to try each element of the dictionary but also change the case of some letters to find the correct password.

This has increased the time of hacking greatly, so using brute force is probably not an option. Use the dictionary of standard passwords, and do not forget to try changing the cases of different letters. For example, there is the word ‘qwerty’ in the dictionary, but the cunning admin sets it to ‘qWeRTy’. Your program should make it possible to hack such passwords, too.

<br/>In this stage, you should write a program that:

1. Parses the command line and gets two arguments that are IP address and port. 
2. Finds the correct password using the list of typical passwords. 
3. Prints the password it found.

Note that here and throughout the project, the password is different every time you check your code


<br/>The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

**Example:**
```
> python hack.py localhost 9090
qWeRTy
```


## <br/>Stage 4:
### _Catching exception_
The server is becoming smarter along with your hacking program. Now the admin has implemented a security system by login and password. In order to access the site with admin privileges, you need to know the admin's login and password. Fortunately, we have a dictionary of different logins and a very interesting vulnerability. You need to improve your program once again to hack the new system.

Also, now the admin has made a complex password that is guaranteed to be absent in the databases since it's randomly generated from several characters.

The server now uses JSON to send messages.

First of all, you should adjust your program so that it can send the combination of login and password in JSON format to the server. Your request should now look like this:

```
{
    "login": "admin",
    "password": "12345678"
}
```
In case of the wrong login, the response you receive looks like this:
In case of the wrong login, the response you receive looks like this:
```
{
    "result": "Wrong login!"
}
```
If you got the login right but failed to find the password, you get this:
```
{
    "result": "Wrong password!"
}
```
If some exception happens, you'll see this result:
```
{
    "result": "Exception happened during login"
}
```
When you finally succeed in finding both the login and the password, you'll see the following:
```
{
    "result": "Connection success!"
}
```
Use the [dictionary of typical admin logins](https://stepik.org/media/attachments/lesson/255258/logins.txt). Since you don’t know the login, you should try different variants from the dictionary the same way you did at the previous stage with the passwords.

**Use an empty password while searching for the correct login. It matters because you will know that the login is correct the moment you get the ‘wrong password’ result instead of ‘wrong login’.**

As for passwords, they’ve become yet harder, so a simple dictionary is no longer enough. Fortunately, a vulnerability has been found: the ‘exception’ message pops up when the symbols you tried for the password match the beginning of the correct one

<br/>Your algorithm is the following:

1. Try all logins with an empty password. 
2. When you find the login, try out every possible password of length 1. 
3. When an exception occurs, you know that you found the first letter of the password. 
4. Use the found login and the found letter to find the second letter of the password. 
5. Repeat until you receive the ‘success’ message.

Finally, your program should print the combination of login and password in JSON format. The examples show two ways of what the output can look like.

<br/>The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> python hack.py localhost 9090
{
    "login" : "superuser",
    "password" : "aDgT9tq1PU0"
}
```

**Example 2:**
```
> python hack.py localhost 9090
{"login": "new_user", "password": "Sg967s"}
```


## <br/>Stage 5:
### _Time-based vulnerability_
Your program has successfully hacked the new system! However, you've been spotted: the admin noticed your first failed attempts, found the vulnerability and made a patch. You should overcome this patch and hack the system again. It’s not easy being a hacker!

The admin has improved the server: the program now catches the exception and sends a simple ‘wrong password’ message to the client even when the real password starts with current symbols.

But here's the thing: the admin probably just caught this exception. We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password

<br/>In this stage, you should write a program that uses the time vulnerability to find the password.

+ Use the list of logins from the previous stage.
+ Output the result as you did this in the previous stage

<br/>The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> python hack.py localhost 9090
{
    "login" : "su",
    "password" : "fTUe3O99Rre"
}
```

**Example 2:**
```
> python hack.py localhost 9090
{"login": "admin3", "password": "mlqDz33x"}
```