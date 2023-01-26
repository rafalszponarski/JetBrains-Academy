# Steps needed to complete project "[**_Currency Converter_**](https://hyperskill.org/projects/157)"

## <br/>Stage 1:
### _Cryptocurrencies are the new black_
Today we start our new project. It will be a simple currency converter. Every person sometimes needs to convert one currency to another. But we need to start easy, so for now, all you need to do is to print "Meet a conicoin!" Please, make sure that the output formatting of your program follows the example output formatting.

&nbsp;

Imagine that there is a cryptocurrency called conicoin ("coni" is just an anagram of the word "coin"). Greet conicoin as shown in the example below.

&nbsp;

**Example:**
```
Meet a conicoin!
```


## <br/>Stage 2:
### _Talking numbers_
Holy moly! Suddenly you remember that back in 2008 you purchased several conicoins! Are you officially rich? Well, we need to find it out. You need to write a program that shows how much you can get after selling your conicoins. One conicoin is 100 dollars. Read your amount of the conicoins as the input, convert them into dollars, and output the result. Also, express your joy, it's important.

&nbsp;

Find out if you are rich.

1. Input the amount of your conicoins. 
2. Calculate the number of dollars you receive after the conversion. 1 conicoin = 100 dollars, print the result as shown below. 
3. Woohoo! You are rich!

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example:**
```
> 42
I have 42 conicoins.
42 conicoins cost 4200 dollars.
I am rich! Yippee!
```


## <br/>Stage 3:
### _More interaction_
We are going to make our program more complex. As you remember, the conicoin rate was fixed in the previous stage. But in the real world, things are different. It's time to write a program that takes your conicoins and an up-to-date conicoin exchange rate, then counts how many dollars you would get, and prints the result.

&nbsp;

1. Get the number of conicoins from the user input. 
2. Get the exchange rate from the user input. 
3. Calculate and print the result.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
Please, enter the number of conicoins you have: > 13
Please, enter the exchange rate: > 2
The total amount of dollars: 26
```

**Example 2:**
```
Please, enter the number of conicoins you have: > 128
Please, enter the exchange rate: > 3.21
The total amount of dollars: 410.88
```


## <br/>Stage 4:
### _Going global_
You can convert your conicoins into dollars, cool. What if you want a different currency? What if you're going to Morocco tomorrow? You'll need some dirhams, that's for sure. We need to improve our converter.

Take the imaginary exchange rates below and modify your program to work with 5 different currencies:

- RUB – Russian Ruble; 1 conicoin = 2.98 RUB; 
- ARS – Argentine Peso; 1 conicoin = 0.82 ARS; 
- HNL – Honduran Lempira; 1 conicoin = 0.17 HNL; 
- AUD – Australian Dollar; 1 conicoin = 1.9622 AUD; 
- MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.

Take the number of conicoins as the user input, сonvert it to the specified currencies, and round the result to two decimals using the Python built-in function. Notice that the input number can have a fractional part!

&nbsp;

1. Get the number of conicoins from user input. 
2. Print how much you will get in all five currencies mentioned above.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> 17
I will get 50.66 RUB from the sale of 17.0 conicoins.
I will get 13.94 ARS from the sale of 17.0 conicoins.
I will get 2.89 HNL from the sale of 17.0 conicoins.
I will get 33.36 AUD from the sale of 17.0 conicoins.
I will get 3.54 MAD from the sale of 17.0 conicoins.
```

**Example 2:**
```
> 3.5
I will get 10.43 RUB from the sale of 3.5 conicoins.
I will get 2.87 ARS from the sale of 3.5 conicoins.
I will get 0.6 HNL from the sale of 3.5 conicoins.
I will get 6.87 AUD from the sale of 3.5 conicoins.
I will get 0.73 MAD from the sale of 3.5 conicoins.
```


## <br/>Stage 5:
### _JSON and the Rates_
In the previous stages, we worked with different real-world currencies but the exchange rates were fixed. Unfortunately (or not, depending on your political stance), we don't really have fixed exchange rates in today's world. At this stage, you will have to work with the Internet to get the information! The [FloatRates](http://www.floatrates.com/json-feeds.html) site contains a special JSON page for each currency. Your task is to make requests to these pages and download the actual data on the exchange rates of the US dollar and the euro. Remember, that the data is stored in JSON format.

&nbsp;

There are many currency codes, for example, RUB, ARS, HNL, AUD, MAD, etc. Your task is to return the information about the exchange rates from the site specified above for a given currency and USD and EUR.

1. Take the currency code as the user input. 
2. Make a request to http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json. Don't forget to replace `YOUR_CURRENCY_CODE` in the link with your currency and put the code in lowercase. 
3. Print your result for USD and EUR.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

> Be aware that the dictionary elements are unordered. The results of your output may differ, as the service updates the data once in twelve hours. Don't hesitate to print the whole string for your own interest, but it is not a part of the stage.

**Example:** The output for HNL:
```
> HNL
{'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 0.040212252288502, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 24.868042526579}
{'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 0.035775653590882, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 27.951970114527}
```


## <br/>Stage 6:
### _Last but not least_
Now your program knows how to get up-to-date rates. Let's make it more interactive! In this stage, you need to read from the input the currency you have, the currency you want to exchange your money for, and the amount of money you want to exchange. Mind that the input number can have a fractional part!

Keep in mind that the currency you have stays the same, you read it only once in the beginning, then you only need to read the currency you want to exchange your money for and the amount of money since they change. If you come across an empty input, the options for exchange are over.

In product development, the performance is key. Let's use a simple way to speed up the program, called **caching**. What if you need to do the math for the same exchange target several times? Isn't it better to save rates at runtime, instead of wasting resources on retrieving the same data from the Internet? If you already did calculations for this exchange target before, you know the rate, so there is no need to connect to the Internet, you only need to refer to the data in cache. You can organize the cache anyway you like, but the easiest way would be to use (as you probably already did in stage 5) a dictionary with currencies as keys and rates as values.

&nbsp;

Let's go over the steps one more time:

1. Take the first input – the currency that you have. It is default for all the calculations. 
2. Retrieve the data from [FloatRates](http://www.floatrates.com/json-feeds.html) as before. 
3. Save the exchange rates for USD and EUR (these are the most popular ones, so it's good to have rates for them in advance). 
4. Take the second input – the currency code that you want to exchange money for, and the third input – amount of money you have. 
5. Check the cache. Maybe you already have what you need? 
6. If you have the currency in your cache, calculate the result. 
7. If not, get it from the site, and calculate the result. 
8. Save the rate to your cache. 
9. Print the result. 
10. Repeat steps 4-9 until there is no currency left to process.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that it's not part of the input.

**Example 1:**
```
> ILS
> USD
> 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.
```

**Example 2:**
```
> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```
