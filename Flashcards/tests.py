from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from typing import List
import os


CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

right_keyword = "correct"
wrong_keyword = "wrong"
goodbye_message = 'bye bye'
filepath = "animal_sounds.txt"
filepath_2 = "capitals.txt"
filepath_3 = "states.txt"
log_filepath = "log.txt"
questions_number = 100

menu = "Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats)"

filepaths = [filepath, filepath_2, filepath_3]

for fp in filepaths:
    if os.path.exists(fp):
        os.remove(fp)

class FlashcardsTest(StageTest):

    is_completed = False

    def generate(self) -> List[TestCase]:
        answers = "Washington\n" * questions_number
        return [TestCase(stdin="exit", check_function=FlashcardsTest.check_menu),
                TestCase(stdin=["add\ncat\nmeow",
                                self.test_output_added_card,
                                self.test_output_existing_card,
                                self.test_output_existing_def,
                                self.test_ask,
                                self.test_first_ask,
                                self.test_wrong_result,
                                self.test_wrong_result_2,
                                self.test_remove,
                                self.test_remove_not_existing,
                                self.test_remove_existing,
                                self.test_export_name,
                                self.test_export,
                                self.test_import_name,
                                self.test_wrong_import,
                                self.test_import,
                                self.test_ask_2,
                                self.test_correct_result,
                                self.test_log_saving,
                                self.test_log]),
                TestCase(stdin=["hardest card",
                                self.test_zero_mistakes,
                                "Canada\nOttawa\n"
                                "add\nJapan\nTokyo\n"
                                "add\nPoland\nWarsaw\n"
                                "ask\n{}\n".format(questions_number) +
                                answers + "hardest card",
                                self.test_randomness,
                                self.test_hardest_after_import,
                                self.test_reset,
                                self.test_hardest_after_reset]),
                TestCase(args=['--export_to={}'.format(filepath_3)],
                         stdin='add\nTexas\nAustin\n'
                                'add\nFlorida\nTallahassee\n'
                                'add\nCalifornia\nSacramento\n'
                                'ask\n3\nAustin\nAustin\nAustin\nexit',
                         check_function=FlashcardsTest.check_sys_export,
                         attach=filepath_3),
                TestCase(args=['--import_from={}'.format(filepath_3)],
                         stdin='remove\nTexas\nremove\nFlorida\nask\n2\nSacramento\nAustin\nexit',
                         check_function=FlashcardsTest.check_sys_import),
                TestCase(args=['--export_to={}'.format(filepath_3),
                               '--import_from={}'.format(filepath_3)],
                         stdin='ask\n1\nAustin\nexit',
                         check_function=FlashcardsTest.check_sys_import_export,
                         attach=filepath_3
                         )
                ]

    @staticmethod
    def check_menu(reply, attach):
        reply = reply.lower()
        if menu.lower() not in reply:
            return CheckResult.wrong("Your program doesn't output the starting message in the required format:\n"
                                     "{0}".format(menu))
        if goodbye_message not in reply:
            return CheckResult.wrong("Your program doesn't output the message \"{0}\" "
                                     "after the 'exit' command".format(goodbye_message))
        return CheckResult.correct()

    def test_output_added_card(self, reply):
        if "has been added" not in reply.lower():
            return CheckResult.wrong("After adding a card with a definition your program should output the message:\n"
                                     "\"The pair (\"term\":\"definition\") has been added.\"")
        if menu.lower() not in reply.lower():
            return CheckResult.wrong("After adding a card with a definition, your program should ask "
                                     "the user for the action again (use the standard menu \"{0}\" for that)."
                                     "".format(menu))
        return "add\ncat"

    def test_output_existing_card(self, reply):
        if "already exists" not in reply.lower():
            return CheckResult.wrong("Your program did not output an error message "
                                     "when the user tried to input a duplicate card. "
                                     "Instead, your program printed this line:\n{}".format(reply))

        return "dog\nmeow"

    def test_output_existing_def(self, reply):
        if "already exists" not in reply.lower():
            return CheckResult.wrong("Your program did not output an error message "
                                     "when the user tried to input a duplicate definition. "
                                     "Instead, your program printed this line:\n{}".format(reply))

        return "woof\nask"

    def test_ask(self, reply):
        lines_split = reply.strip().split('\n')
        if "many times to ask" not in reply.lower():
            return CheckResult.wrong("Before asking the definitions of cards, your program should"
                                     "ask: \"How many times to ask?\". These words were not found"
                                     "in the output of your program:\n"
                                     "{0}".format(lines_split[-1] if len(lines_split) > 0 else reply))
        return "2"

    def test_first_ask(self, reply):
        lines_split = reply.strip().split('\n')
        if "print the definition of" not in reply.lower():
            return CheckResult.wrong("Your program did not ask the user to print the definition of the card.\n")
        if "cat" not in reply.lower() and "dog" not in reply.lower():
            return CheckResult.wrong("Your program did not ask for the definition of any of existing cards:\n"
                                     "{0}".format(lines_split[-1] if len(lines_split) > 0 else reply))
        if "cat" in reply.lower():
            return "woof"
        else:
            return "meow"

    def test_wrong_result(self, reply):
        lines_split = reply.strip().split('\n')
        if "wrong" not in reply.lower():
            return CheckResult.wrong("The user gave a wrong answer, but the word \"wrong\" was not "
                                     "found in the reply of your program:\n"
                                     "{0}".format(lines_split[0] if len(lines_split) > 0 else reply))

        if "but your definition is correct" not in reply.lower():
            return CheckResult.wrong("The user gave a wrong answer that was correct for another card."
                                     "Your program should notify the user about this by printing\n"
                                     "\"Wrong. The right answer is \"{card}\", "
                                     "but your definition is correct for \"{another card}\"\"")

        if "print the definition" not in reply.lower():
            return CheckResult.wrong("Your program did not ask for the definition of a card for the second time.")

        if "cat" not in reply.lower() and "dog" not in reply.lower():
            return CheckResult.wrong("Your program did not ask for the definition of any of existing cards:\n"
                                     "{0}".format(lines_split[-1] if len(lines_split) > 0 else reply))

        return "wapapapapow"

    def test_wrong_result_2(self, reply):
        lines_split = reply.strip().split('\n')
        if "wrong" not in reply.lower():
            return CheckResult.wrong("The user gave a wrong answer, but the word \"wrong\" was not "
                                     "found in the reply of your program:\n"
                                     "{0}".format(lines_split[0] if len(lines_split) > 0 else reply))
        if "input the action" not in reply.lower():
            return CheckResult.wrong("After asking the required number of definitions, your program"
                                     " should ask the user for the action again "
                                     "(use the standard menu \"{0}\" for that).".format(menu))
        return "remove"

    def test_remove(self, reply):
        if "which card" not in reply.lower():
            return CheckResult.wrong("The program should ask \"Which card?\" when the user enters "
                                     "\"remove\" action")
        return "badger"

    def test_remove_not_existing(self, reply):
        reply = reply.lower()
        if "can't remove" not in reply or "no such card" not in reply:
            return CheckResult.wrong("When the user tries to remove a non-existent card, "
                                     "your program should output a message "
                                     "\"Can't remove \"{card name}\": there is no such card.\"")
        if "input the action" not in reply:
            return CheckResult.wrong("After unsuccessful attempt of removing a card, "
                                     "your program should suggest the user to choose an action again. "
                                     "Use the standard menu \"{0}\" for that.".format(menu))

        return "remove\ncat"

    def test_remove_existing(self, reply):
        if "has been removed" not in reply.lower():
            return CheckResult.wrong("After the user inputs a name of the card that should be removed,"
                                     "your program should remove it and output a message\n:"
                                     "\"The card has been removed.\"")
        if "input the action" not in reply.lower():
            return CheckResult.wrong("After removing a card, "
                                     "your program should suggest the user to choose an action again. "
                                     "Use the standard menu \"{0}\" for that.".format(menu))
        return "add\nhorse\nneigh\nexport"

    def test_export_name(self, reply):
        if "file" not in reply.lower():
            return CheckResult.wrong("Your program did not ask for the name of the file "
                                     "where the exported cards should be saved.")
        return filepath

    def test_export(self, reply):
        if "2 cards have been saved" not in reply.lower():
            return CheckResult.wrong("The user commanded to export cards, but the program did not "
                                     "output a correct message \"{n} cards have been saved\". "
                                     "Make sure that the number of cards is calculated and written correctly.")
        if not os.path.exists(filepath):
            return CheckResult.wrong("The file where the cards should have been exported is not found. "
                                     "Make sure you saved the file correctly.")
        return "import"

    def test_import_name(self, reply):
        if "file" not in reply.lower():
            return CheckResult.wrong("Your program did not ask for the name of the file "
                                     "where the imported cards should be loaded from.")
        return "ghost_file.txt"

    def test_wrong_import(self, reply):
        if "not found" not in reply.lower():
            return CheckResult.wrong("If the user tries to import cards from a non-existent file, "
                                     "your program should output a message \"File not found.\"")
        if "input the action" not in reply.lower():
            return CheckResult.wrong("After unsuccessful attempt of importing cards, "
                                     "your program should suggest the user to choose an action again. "
                                     "Use the standard menu \"{0}\" for that.".format(menu))
        return "import\n{}".format(filepath)

    def test_import(self, reply):
        if "2 cards have been loaded" not in reply.lower():
            return CheckResult.wrong("Your program should have imported cards from a file and output a message:\n"
                                     "\"{n} cards have been loaded.\" "
                                     "Check if the message is printed in the correct format "
                                     "and the number of cards is calculated correctly.")
        try:
            os.remove(filepath)
        except PermissionError:
            return CheckResult.wrong("Impossible to remove the file with the exported cards. "
                                     "Perhaps you haven't closed this file?")
        except FileNotFoundError:
            return CheckResult.wrong("A file from which the cards should have been imported is not found. "
                                     "Make sure you did not delete the file after importing the cards.")

        return "ask\n1"

    def test_ask_2(self, reply):
        if "dog" not in reply.lower() and "horse" not in reply.lower():
            return CheckResult.wrong("Your program did not ask for the definition of any of the existing cards.")
        if "dog" in reply.lower():
            return "woof"
        else:
            return "neigh"

    def test_correct_result(self, reply):
        if right_keyword not in reply.lower():
            return CheckResult.wrong("The user gave a correct answer, but the program did not output a message "
                                     "with the word \"{}\"".format(right_keyword))
        if "input the action" not in reply.lower():
            return CheckResult.wrong("After asking the required number of definitions, "
                                     "your program should suggest the user to choose an action again. "
                                     "Use the standard menu \"{0}\" for that.".format(menu))
        return "log"

    def test_log_saving(self, reply):
        if "file" not in reply.lower():
            return CheckResult.wrong("When the user wants to save the log, the program should ask for "
                                     "the name of the file where log should be saved.")
        return log_filepath

    def test_log(self, reply):
        if not os.path.exists(log_filepath):
            return CheckResult.wrong("The file with the log has not been found. "
                                     "Make sure that you correctly saved the log file.")
        if "log has been saved" not in reply.lower():
            return CheckResult.wrong("When the log is saved, "
                                     "the program should output a message \"The log has been saved.\"")
        try:
            os.remove(log_filepath)
        except PermissionError:
            return CheckResult.wrong("Impossible to remove the file with the log. "
                                     "Perhaps you haven't closed this file?")
        self.is_completed = True
        return "exit"

    def test_zero_mistakes(self, reply):
        if 'no cards with errors' not in reply:
            return CheckResult.wrong("The user ask to output the hardest card. Since no questions were asked yet, "
                                     "the output \"There are no cards with errors.\" was expected. \n"
                                     "However, it was not found. \n"
                                     "Make sure your program correctly counts the number of mistakes that were made.")
        return "add"

    def test_randomness(self, reply):
        reply = reply.lower()
        quiz_start_index = reply.find("print the definition of")
        reply = reply[quiz_start_index:]

        if "the hardest card is" not in reply or "errors" not in reply or "answering it" not in reply:
            return CheckResult.wrong("The line naming the hardest card and stating the number of mistakes "
                                     "made for this card was expected in the output of your program.\n"
                                     "However, it was not found. Make sure you use the correct formatting of your output.")

        quiz_end_index = reply.find("the hardest card is")
        quiz = reply[:quiz_end_index]

        questions_found = quiz.count("print the definition of")
        if questions_found != questions_number:
            return CheckResult.wrong("The program did not ask the user "
                                     "for the definition of a card for the required number of times.\n"
                                     "Make sure that your program reads correctly the input specifying the number of times to ask. \n"
                                     "Also make sure that it is able to ask definitions more than once:\n"
                                     "for example, even if there are only 3 cards added, your program still "
                                     "should be able to ask the user for 100 times.")
        japan_asked_n = quiz.count("japan")
        canada_asked_n = quiz.count("canada")
        poland_asked_n = quiz.count("poland")
        minimum_asked = questions_number // 6

        if japan_asked_n < minimum_asked or canada_asked_n < minimum_asked or poland_asked_n < minimum_asked:
            return CheckResult.wrong("It looks like during the quiz your program does not choose the cards randomly.\n "
                                     "Make sure your program uses the random module to choose which definition "
                                     "it'll ask the user to give.\n"
                                     "If you're sure that you choose the cards randomly, try to rerun the tests.")

        asked_n = {'japan': japan_asked_n, 'canada': canada_asked_n, 'poland': poland_asked_n}
        sorted_keys = sorted(asked_n.keys(), key=lambda x:asked_n[x])
        n_wrong = asked_n[sorted_keys[-1]]
        max_wrong = [key for key in asked_n.keys() if asked_n[key] == n_wrong]

        hardest_card_line = reply[reply.find("the hardest card is"):reply.find("answering it")]
        if str(n_wrong) not in hardest_card_line:
            return CheckResult.wrong("Seems like your program incorrectly calculated "
                                     "the number of errors for the hardest card.")

        if not any(card_name in hardest_card_line for card_name in max_wrong):
            return CheckResult.wrong("Seems like your program incorrectly identified the card with "
                                     "the maximum number of errors.")

        return "export\n{0}\nimport\n{0}\nhardest card".format(filepath_2)

    def test_hardest_after_import(self, reply):
        try:
            os.remove(filepath_2)
        except PermissionError:
            return CheckResult.wrong("Impossible to remove the file with the exported cards. "
                                     "Perhaps you haven't closed this file?")
        except FileNotFoundError:
            return CheckResult.wrong("A file from which the cards should have been imported is not found. "
                                     "Make sure you did not delete the file after importing the cards.")

        reply = reply.lower()
        if "the hardest card is" not in reply or "errors" not in reply or "answering it" not in reply:
            return CheckResult.wrong("The line naming the hardest card and stating the number of mistakes "
                                     "made for this card was expected in the output of your program.\n"
                                     "However, it was not found. \n"
                                     "Make sure that your program saves the number of mistakes for each card while exporting them,\n"
                                     "and loads the cards and the number of mistakes for them correctly during the import.")
        return "reset stats"

    def test_reset(self, reply):
        if "have been reset" not in reply.lower():
            return CheckResult.wrong("The line \"Card statistics have been reset.\" was expected in the output "
                                     "after the user entered \"reset stats\", but it was not found there.")
        return "hardest card"

    def test_hardest_after_reset(self, reply):
        if "no cards with errors" not in reply.lower():
            return CheckResult.wrong("After the reset of stats, "
                                     "the line \"There are no cards with errors.\" is expected\n"
                                     "when the program is asked about the hardest card.\n"
                                     "However, your program does not seem to respond to this command correctly.")
        self.is_completed = True
        return "exit"

    @staticmethod
    def check_sys_export(reply, attach):
        if "cards have been saved" not in reply.lower():
            return CheckResult.wrong("The user has provided the --export_to command-line argument. \n"
                                     "So, after the user inputs the command \"exit\", \n"
                                     "your program should save the cards to the file specified in the command-line argument\n."
                                     "After that, a message about the number of cards that have been saved should be printed by your program.\n"
                                     "However, this message was not found.")
        if "3 cards have been saved" not in reply.lower():
            return CheckResult.wrong("Seems like your program incorrectly printed the number of cards "
                                     "exported to file after \"exit\" command.")
        if not os.path.exists(attach):
            return CheckResult.wrong("The user has provided the --export_to command-line argument. \n"
                                     "However, the file where the cards should have been exported after \"exit\" was not found. "
                                     "Make sure you named the file with exported cards "
                                     "as was required in --export_to command-line argument.")

        return CheckResult.correct()

    @staticmethod
    def check_sys_import(reply, attach):
        reply = reply.lower()
        if "cards have been loaded" not in reply:
            return CheckResult.wrong("The user has provided the --import_from command-line argument. \n"
                                     "So, in the beginning of the game, \n"
                                     "your program should load the cards from the file specified in the command-line argument\n."
                                     "After that, a message about the number of cards that have been loaded should be printed by your program.\n"
                                     "However, this message was not found.")
        if "3 cards have been loaded" not in reply:
            return CheckResult.wrong("Seems like your program incorrectly printed the number of cards "
                                     "imported from the file in the beginning of the game.")
        if reply.count("has been removed") != 2:
            return CheckResult.wrong("Your program was asked to remove several existing cards, \n"
                                     "however, it seems that it did not do it, \n"
                                     "or did not output the message \"The card has been removed.\"")
        if right_keyword not in reply:
            return CheckResult.wrong("The user gave a correct answer, "
                                     "but your program did not output the word \"{}\".".format(right_keyword))
        if wrong_keyword not in reply:
            return CheckResult.wrong("The user gave a wrong answer, "
                                     "but your program did not output the word \"{}\".".format(wrong_keyword))

        return CheckResult.correct()

    @staticmethod
    def check_sys_import_export(reply, attach):
        reply = reply.lower()
        if "cards have been loaded" not in reply:
            return CheckResult.wrong("The user has provided the --import_from command-line argument. \n"
                                     "So, in the beginning of the game, \n"
                                     "your program should load the cards from the file specified in the command-line argument\n."
                                     "After that, a message about the number of cards that have been loaded should be printed by your program.\n"
                                     "However, this message was not found.")
        if "3 cards have been loaded" not in reply:
            return CheckResult.wrong("Seems like your program incorrectly printed the number of cards "
                                     "imported from the file in the beginning of the game.")

        if right_keyword not in reply and (wrong_keyword not in reply and "but your definition is correct for"):
            return CheckResult.wrong("Your program did not respond correctly to the user's answer on the question.\n"
                                     "Make sure you've imported cards from the file specified in the --import_from command-line argument.")
        if "cards have been saved" not in reply.lower():
            return CheckResult.wrong("The user has provided the --export_to command-line argument. \n"
                                     "So, after the user inputs the command \"exit\", \n"
                                     "your program should save the cards to the file specified in the command-line argument\n."
                                     "After that, a message about the number of cards that have been saved should be printed by your program.\n"
                                     "However, this message was not found.")
        if "3 cards have been saved" not in reply.lower():
            return CheckResult.wrong("Seems like your program incorrectly printed the number of cards "
                                     "exported to file after \"exit\" command.")
        if not os.path.exists(attach):
            return CheckResult.wrong("The user has provided the --export_to command-line argument. \n"
                                     "However, the file where the cards should have been exported after \"exit\" was not found. "
                                     "Make sure you named the file with exported cards "
                                     "as was required in --export_to command-line argument.")
        try:
            os.remove(attach)
        except PermissionError:
            return CheckResult.wrong("Impossible to remove the file with the exported cards. "
                                     "Perhaps you haven't closed this file?")
        return CheckResult.correct()

    def check(self, reply, attach):
        if self.is_completed:
            self.is_completed = False
            return CheckResult.correct()
        else:
            return CheckResult.wrong('Your program did not read all inputs!')


if __name__ == "__main__":
    FlashcardsTest("flashcards.flashcards").run_tests()
