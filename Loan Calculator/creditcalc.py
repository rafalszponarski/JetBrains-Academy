from argparse import ArgumentParser
from math import ceil, log, floor

parser = ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", help="Type annuity or diff")
parser.add_argument("--principal", type=int, help="Loan principal")
parser.add_argument("--periods", type=int, help="Months to repay")
parser.add_argument("--payment", type=int, help="Annuity payment")
parser.add_argument("--interest", type=float, help="Rate of interest")
args = parser.parse_args()

if list(vars(args).values()).count(None) != 1:
    print("Incorrect parameters")
    exit()

match args.type:
    case 'annuity':
        if not args.periods:
            i = args.interest / (100 * 12)
            months = floor(log((args.payment / (args.payment - i * args.principal)), i+1)) + 1
            overpay = months * args.payment - args.principal
            years = months // 12
            months -= years * 12

            print(f"It will take {years if years else months} {'years' if years else 'months'}\
            {' and ' + str(months) + ' months' if months and years else ''} to repay this loan!")
            print(f"Overpayment = {overpay}")

        elif not args.payment:
            i = args.interest / (100 * 12)
            payment = ceil(args.principal * (i * ((1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1)))

            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {payment * args.periods - args.principal}")

        elif not args.principal:
            i = args.interest / (100 * 12)
            first = i * ((1 + i) ** args.periods)
            principal = floor(args.payment / (first / (first / i - 1)))

            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {args.periods * args.payment - principal}")

    case 'diff':
        if None in (args.principal, args.periods, args.interest):
            print("Incorrect parameters")
            exit()

        total = 0
        for i in range(args.periods):
            term = args.interest / (100 * 12) * (args.principal - ((args.principal * i) / args.periods))
            diff = ceil(args.principal / args.periods + term)
            total += diff

            print(f"Month {i}: payment is {diff}")
        print(f"Overpayment = {total - args.principal}")
