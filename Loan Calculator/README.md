# Steps needed to complete project "[**_Loan Calculator_**](https://hyperskill.org/projects/90)"

## <br/>Stage 1:
### _Beginning_
Let's think about what a loan calculator should be able to do. In general, it takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.

Not familiar with these concepts? Don't worry, we will explain them to you in simple terms. The principal is the original amount of money you borrow. The interest is a charge for borrowing that money, usually calculated as a percentage of the principal amount.

&nbsp;

Let's start by imitating this behavior. There are some prepared variables in the source code: these are text messages that our loan calculator can output. In this stage, all you need to do is output them in the right order.

&nbsp;

**Example:**
```
Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!
```


## <br/>Stage 2:
### _Dreamworld_

If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.

Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.

In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.

Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:

payment = principal / months = 1000 / 9 = 111.11...

Of course, you can't pay that amount of money since it's a float value. You have to round up this value and make it 112. But why do we round it up instead of rounding it down? Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

lastpayment = principal - (periods-1) * payment = 1000 - 8 * 112 = 104

In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

&nbsp;

The behavior of your program should look like this:

- Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount. 
- To perform further calculations, you'll also have to ask for the required missing value. 
- Finally, output the results for the user.

> When you output how many months it will take to repay the loan, mind the grammar of the sentence. For example, if it will take just one month to repay it, you should output: `"It will take 1 month to repay the loan"` (using the singular form of `"month"`). In other cases, use the plural form of `"month"`: `"It will take 7 months to repay the loan"`.

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that this is not part of the input.

**Example 1:**
```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
```

**Example 2:**
```
Enter the loan principal:
> 1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It will take 1 month to repay the loan
```

**Example 3:**
```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 10

Your monthly payment = 100
```

**Example 4:**
```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104.
```

## <br/>Stage 3:
### _Annuity payment_
Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the former. `Annuity` type of payment consists in paying a fixed sum of money at specified intervals, for example, each month or each year. The `annuity payment` amount is precisely this fixed sum of money that you need to pay at regular intervals.

Let's assume that annuity payments are made monthly. Thus, we can use the following formula to calculate the `monthly payment`:

A_ordinary_annuity = P * (i * (1+i)^n) / ((1+i)^n - 1)

Where:

**A** = annuity payment;

**P** = loan principal;

**i** = nominal (monthly) interest rate. Usually, it is 1/12 of the annual interest rate and is a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;

**n** = number of payments. This is usually the number of months in which repayments will be made.

So far, in this stage you are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can be calculated if others are known:

**Loan principal:**

P = A / ( (i * (1+i)^n) /  ((1+i)^n - 1) )

**The number of payments:**

n = log(1+i) (A / A-i*P)

&nbsp;

In this stage, you should add new behavior to the calculator:

First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
Then, you need to ask them to input the remaining values.
Finally, compute and output the value that they wanted.
Note that you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:

The first is the loan principal (`P` in the formulas).
The second is the monthly payment (`A` in the formulas).
The next is the number of monthly payments (`n` in the formulas).
The last is the loan interest. The user inputs the interest rate as a percentage, for example, 11.7. You should divide this value by 12 and 100 to use it as i in the formula.
Please be careful converting `"X months"` to `"Y years and Z months"`. Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that this is not part of the input.

**Example 1:** calculating the number of monthly payments
```
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> n
Enter the loan principal:
> 1000000
Enter the monthly payment:
> 15000
Enter the loan interest:
> 10
It will take 8 years and 2 months to repay this loan!
```

Let’s take a closer look at **Example 1**.

You know the loan principal, the loan interest, and the monthly payment (annuity payment). You want to calculate the number of monthly payments. What do you do?

1) You need to know the nominal interest rate. It is calculated like this:

i = 10% / 12*100% = 0.008333...

2) Now you can calculate the number of months:

n = log(1 + 0.008333...) (15000 / 15000-0.008333...*1000000) = 97.71...

3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and in the 98th month the user will pay 0.71... of the monthly payment. So, there are 98 months to pay. 

n = 98

4) Finally, you need to convert “98 months” to “8 years and 2 months” so that it is more readable and understandable for the user.

**Example 2:** calculating the monthly payment (the annuity payment)
```
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> a
Enter the loan principal:
> 1000000
Enter the number of periods:
> 60
Enter the loan interest:
> 10
Your monthly payment = 21248!
```

**Example 3:** calculating the loan principal
```
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> p
Enter the annuity payment:
> 8721.8
Enter the number of periods:
> 120
Enter the loan interest:
> 5.6
Your loan principal = 800000!
```

## <br/>Stage 4:
### _Differentiate payment_
Finally, let's add to our calculator the capacity to compute `differentiated payments`. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. Let’s look at the formula:

Dm = P/n+i*( P-P*(m-1) / n)

Where:

`Dm` = mth differentiated payment;

`P` = the loan principal;

`i` = nominal interest rate. This is usually 1/12 of the annual interest rate and is a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.

`n` = number of payments. This is usually the number of months in which repayments will be made.

`m` = current repayment month.

In this stage, the user has to input a lot of parameters, so it might be convenient to use command-line arguments. The argparse module can help you parse them. You can run your loan calculator via command line like this:

`python creditcalc.py`

Using command-line arguments you can run your program this way:

`> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10`

Check the description and examples below for more details.

&nbsp;

In this stage, you are going to implement the following features:

- Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
- Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
- Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).

The final version of your program is supposed to work from the command line and parse the following parameters:

- `--type` indicates the type of payment: `"annuity"` or `"diff"` (differentiated). If `--type` is specified neither as `"annuity"` nor as `"diff"` or not specified at all, show the error message.
```
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters
```

- `--payment` is the monthly payment amount. For `--type=diff`, the payment is different each month, so we can't calculate months or principal, therefore a combination with `--payment` is invalid, too:
```
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
```

- `--principal` is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
- `--periods` denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
- `--interest` is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing:
```
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
```

You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:
```
> python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
```

You should also display an error message when negative values are entered:
```
> python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
```

The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!

&nbsp;

The greater-than symbol followed by a space (`>`) represents the user input. Note that this is not part of the input.

**Example 1:** calculating differentiated payments
```
> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
```
In this example, the user wants to take a loan with differentiated payments. You know the principal, the count of periods, and interest, which are 1,000,000, 10 months, and 10%, respectively.

The calculator should calculate payments for all 10 months. Let’s look at the formula above. In this case:

P = 1000000
n = 10

i = interest / 12*100% = 10% / 12*100% = 0.008333...

Now let’s calculate the payment for the first month:

D1 = P/n+i*( P-P*(m-1) / n) = 1000000/10+0.008333...*( 1000000-(1000000*(1-1) / 10) ) = 108333.333...

The second month (m = 2):
D2 = P/n+i*( P-P*(m-1) / n) = 1000000/10+0.008333...*( 1000000-(1000000*(2-1) / 10) ) = 107500

The third month (m = 3):
D3 = P/n+i*( P-P*(m-1) / n) = 1000000/10+0.008333...*( 1000000-(1000000*(3-1) / 10) ) = 106666.666...

And so on. You can see other monthly payments above.

> Your loan calculator should output monthly payments for every month as in the first stage. Also, round up all floating-point values.

Finally, your loan calculator should add up all the payments and subtract the loan principal so that you get the overpayment.

**Example 2:** calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest
```
> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
```

**Example 3:** fewer than four arguments are given
```
> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
```

**Example 4:** calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%
```
> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628
```

**Example 5:** calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest
```
> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622
```

**Example 6:** calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest
```
> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000
```
