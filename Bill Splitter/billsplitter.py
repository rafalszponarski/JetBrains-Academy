from random import choice


party = {}
members = int(input("Enter the number of friends joining (including you):\n"))

if members > 0:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(members):
        party[input()] = 0

    bill = int(input("\nEnter the total bill value:\n"))
    feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if feature.lower() == 'yes':
        lucky = choice(list(party.keys()))
        print(f"\n{lucky} is the lucky one!")

        for name in party.keys():
            if name != lucky:
                party[name] = round(bill/(members-1), 2)

        print(f"\n{party}")

    else:
        print("No one is going to be lucky")
        for name in party.keys():
            party[name] = round(bill/members, 2)

        print(f"\n{party}")
else:
    print("No one is joining for the party")
