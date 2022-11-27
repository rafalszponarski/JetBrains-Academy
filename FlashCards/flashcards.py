from argparse import ArgumentParser
from json import dumps, loads


class FlashCards:
    def __init__(self, import_from, export_to):
        self.imp = import_from
        self.exp = export_to
        self.cards = {}
        self.log = []

    def play(self):
        while True:
            action = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            match action:

                case 'add':
                    while True:
                        card_name = input("The card:")
                        if card_name in self.cards.keys():
                            print(f"The card {card_name} already exists. Try again:")
                        else:
                            break

                    while True:
                        definition = input("The definition of the card:")
                        if definition in [value[0] for value in self.cards.values()]:
                            print(f"The definition {definition} already exists. Try again:")
                        else:
                            break

                    self.cards.update({card_name: [definition, 0]})
                    print(f"The pair ({card_name}:{definition}) has been added.")

                case 'remove':
                    remove_card = input("Which card?")
                    try:
                        self.cards.pop(remove_card)
                        print("The card has been removed.")
                    except KeyError:
                        print(f"Can't remove {remove_card}: there is no such card.")

                case 'import':
                    self.import_cards(None)

                case 'export':
                    filename = input("File name:") if not self.exp else self.exp
                    with open(f"{filename}", "w") as file:
                        file.write(dumps(self.cards))
                    print(f"{len(self.cards)} cards have been saved.")

                case 'ask':
                    self.get_cards(int(input("How many times to ask?")))

                case 'exit':
                    print("Bye bye!")
                    with open(f"{self.exp}", "w") as file:
                        file.write(dumps(self.cards))
                    print(f"{len(self.cards)} cards have been saved.")
                    break

                case 'log':
                    filename = input("File name:")
                    self.log.append(filename)
                    for item in self.log:
                        with open(f"{filename}", 'a') as file:
                            file.write(item.strip() + '\n')
                    print("The log has been saved.")

                case 'hardest card':
                    s_cards = sorted(self.cards.items(), key=lambda x: x[1][1], reverse=True)
                    if len(s_cards) == 0 or s_cards[0][1][1] == 0:
                        print("There are no cards with errors.")
                    else:
                        while True:
                            if s_cards[0][1][1] > s_cards[-1][1][1]:
                                del s_cards[-1]
                            else:
                                break
                    if len(s_cards) == 1:
                        print(f"The hardest card is {s_cards[0][0]}. You have {s_cards[0][1][1]} errors answering it")
                    elif len(s_cards) > 1:
                        cards = ", ".join([f"{item[0]}" for item in s_cards])
                        print(f"The hardest cards are {cards}")

                case 'reset stats':
                    for value in self.cards.values():
                        value[1] = 0
                    print("Card statistics have been reset.")

    def get_cards(self, ask):
        i = 0
        card = ''
        for key, value in self.cards.items():
            answer = input(f"Print the definition of {key}:")
            if answer == value[0]:
                print("Correct!")
            else:

                for k, v in self.cards.items():
                    if v[0] == answer:
                        card = k

                self.cards[key][1] += 1
                if card:
                    print(f"Wrong. The right answer is {value[0]}, but your definition is correct for {card}.")
                else:
                    print(f"Wrong. The right answer is {value[0]}.")
            i += 1
            if i == ask:
                break
        if i < ask:
            self.get_cards(ask - i)

    def import_cards(self, filename):
        filename = input("File name:") if not filename else filename
        try:
            with open(f"{filename}") as file:
                line = file.read().strip()
            new_cards = loads(line)
            for card in new_cards:
                self.cards.update({card: new_cards[card]})
            print(f"{len(new_cards)} cards have been loaded.")
        except FileNotFoundError:
            print("File not found.")


parser = ArgumentParser(description='FlashCards game')
parser.add_argument('--import_from', type=str)
parser.add_argument('--export_to', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    game = FlashCards(args.import_from, args.export_to)
    if args.import_from:
        game.import_cards(args.import_from)
    game.play()
