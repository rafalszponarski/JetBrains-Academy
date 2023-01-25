import os

from hstest.check_result import CheckResult
from hstest.exceptions import WrongAnswerException
from hstest.stage_test import StageTest
from hstest.test_case import TestCase

MAIN_MENU = """
1. Add flashcards
2. Practice flashcards
3. Exit"""
SUB_MENU = """
1. Add a new flashcard
2. Exit"""
UPDATE_MENU = """
press "d" to delete the flashcard:
press "e" to edit the flashcard:
"""
CHECK_LEARN_MENU = """
press "y" if your answer is correct:
press "n" if your answer is wrong:
"""
FIRST_QUESTION = "What is the Capital city of Germany?"
FIRST_ANSWER = "Berlin"
SECOND_QUESTION = "What is the Capital city of Italy?"
SECOND_ANSWER = "Rome"
NEW_SECOND_QUESTION = "Italy?"
NEW_SECOND_ANSWER = "Rome is the capital of Italy"
Q_S = """
press "y" to see the answer:
press "n" to skip:
press "u" to update:
"""
if os.path.exists('flashcard.db'):
    os.remove('flashcard.db')


class FlashCardTest(StageTest):
    def generate(self):
        return [
            TestCase(stdin=[self.test1_input1,
                            self.test1_input2,
                            self.test1_input3,
                            self.test1_input4,
                            self.test1_input5,
                            self.test1_input6,
                            self.test1_input7,
                            self.test1_input8,
                            self.test1_input9,
                            self.test1_input10,
                            'n',
                            self.test1_input11,
                            self.test1_input12,
                            ]),
            # AFTER TEST 1
            # FIRST_QUESTION SHOULD BE IN THE BOX 1
            # SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=[self.test2_input1,
                            self.test2_input2,
                            self.test2_input3]),
            # AFTER TEST 2
            # FIRST_QUESTION SHOULD BE IN THE BOX 1
            # SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['1',
                            '4',
                            self.test3_input1,
                            self.test3_input2]),
            # AFTER TEST 3
            # FIRST_QUESTION SHOULD BE IN THE BOX 1
            # SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['1',
                            '1',
                            ' ',
                            self.test4_input4,
                            self.test4_input5]),
            # AFTER TEST 4
            # FIRST_QUESTION SHOULD BE IN THE BOX 1
            # SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['1',
                            '1',
                            'What is the capital city of Peru?',
                            ' ',
                            self.test5_input5,
                            self.test5_input6]),
            # AFTER TEST 5
            # FIRST_QUESTION SHOULD BE IN THE BOX 1
            # SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['2',
                            self.test1_input10,
                            'n',
                            self.test1_input11,
                            self.test1_input12
                            ]),
            # AFTER TEST 6
            # FIRST_QUESTION SHOULD BE IN THE BOX 1
            # SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['2',
                            'u',
                            self.test7_input3,
                            'u',
                            'e',
                            self.test7_input6,
                            self.test7_input7,
                            self.test7_input8]),
            # AFTER TEST 7
            # FIRST_QUESTION SHOULD BE REMOVED
            # SECOND_QUESTION SHOULD BE REPLACED AS NEW_SECOND_QUESTION AND LOCATED IN THE BOX 1
            TestCase(stdin=['2',
                            self.test8_input2,
                            self.test8_input3]),
            # AFTER TEST 8
            # NEW_SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['2',
                            'y',
                            self.test9_input3]),
            # AFTER TEST 9
            # NEW_SECOND_QUESTION SHOULD BE IN THE BOX 1
            TestCase(stdin=['2',
                            'n',  # SHOULD BE SKIPPED
                            '2',
                            'y',
                            'y',  # SHOULD BE MOVED TO THE BOX 2
                            '2',
                            'y',
                            'y',  # SHOULD BE MOVED TO THE BOX 3
                            '2',
                            'n',  # SHOULD BE SKIPPED
                            '2',
                            'y',
                            'y',  # SHOULD BE REMOVED
                            '2',
                            self.test10_input11]),
            # AFTER TEST 10
            # QUESTIONS SHOULD BE EMPTY
            TestCase(stdin=['1',
                            '1',
                            FIRST_QUESTION,
                            FIRST_ANSWER,
                            '2',
                            '2',  # START PRACTICE WITH FIRST_QUESTION
                            'n',  # SHOULD BE SKIPPED
                            '2',
                            'y',
                            'y',  # SHOULD BE MOVED TO THE BOX 2
                            '2',
                            'y',
                            'y',  # SHOULD BE MOVED TO THE BOX 3
                            '2',
                            'n',  # SHOULD BE SKIPPED
                            '2',
                            'y',
                            'n',  # SHOULD BE MOVED TO THE BOX 1
                            '2',
                            'y',
                            'y',  # SHOULD BE MOVED TO THE BOX 2
                            '2',
                            'y',
                            'y',  # SHOULD BE MOVED TO THE BOX 3
                            '2',
                            'y',
                            'y',  # SHOULD BE REMOVED
                            '2',
                            self.test10_input11]),
            # AFTER TEST 11
            # QUESTIONS SHOULD BE EMPTY
        ]

    def check_main_menu(self, out):
        main_menu_list = MAIN_MENU.strip().split('\n')
        out_list = out.strip().split('\n')
        if len(out_list) > 4 or len(out_list) < 3:
            raise WrongAnswerException(f'The main menu has "3" lines and it must be like this:\n{MAIN_MENU}')
        for index, action in enumerate(main_menu_list):
            if not action == out_list[index]:
                raise WrongAnswerException(f'the line no.{index + 1} of main menu must be like this:\n {action}')
        return True

    def check_sub_menu(self, out):
        sub_menu_list = SUB_MENU.strip().split('\n')
        out_list = out.strip().split('\n')
        if len(out_list) > 3 or len(out_list) < 2:
            raise WrongAnswerException(f'The sub_menu has "2" lines and it must be like this:\n{SUB_MENU}')
        for index, content in enumerate(sub_menu_list):
            if not content == out_list[index]:
                raise WrongAnswerException(f'The line no.{index + 1} must be like this:\n{sub_menu_list[index]}')
        return True

    def check_question(self, out):
        if not "Question:" in out:
            raise WrongAnswerException(f'the word {out} spelling is wrong, it should be like this:\nQuestion:')
        return True

    def check_answer(self, out):
        if not "Answer:" in out:
            raise WrongAnswerException(f'the word {out} spelling is wrong it should be like this:\nAnswer:')
        return True

    def check_practice_question(self, out, question):
        out_list = out.strip().split('\n')
        if len(out_list) < 2:
            raise WrongAnswerException("output can't be empty")
        else:
            out_first_line = out_list[0].split(':')
            if len(out_first_line) == 0:
                raise WrongAnswerException("output can't be empty")
            else:
                if not 'Question' == out_first_line[0]:
                    raise WrongAnswerException(
                        f'The line \"{out_first_line[0]}\" is wrong!\nPlease check extra spaces, misspelling or ":"')
                if len(out_list) < 4:
                    raise WrongAnswerException("Incorrect number of lines is found for the menu after the question \n"
                                               f"\"{out_first_line[0]}\"\n"
                                               f"Please, format your output according to the example.")
                question_menu = f'{out_list[1]}\n{out_list[2]}\n{out_list[3]}'
                if not question == out_first_line[1].strip():
                    raise WrongAnswerException('wrong question is printed')
                if not Q_S.strip() == question_menu.strip():
                    raise WrongAnswerException(f'{question_menu} is wrong\n{Q_S} is correct')
                return True

    def check_practice_answer(self, out, answer):
        out_list = out.strip().split('\n')
        q_s_list = Q_S.strip().split('\n')
        if len(out_list) == 0:
            raise WrongAnswerException("output can't be empty")
        else:
            first_part = out_list.pop(0).strip().split(':')
            if len(first_part) == 0:
                raise WrongAnswerException("output can't be empty")
            else:
                if not 'Answer' == first_part[0]:
                    raise WrongAnswerException('Answer:\n is missing or misspelling!')
                if not answer == first_part[1].strip():
                    raise WrongAnswerException('The answer is not printed correctly')
                if q_s_list[0] in out_list and q_s_list[1] in out_list and q_s_list[2] in out_list:
                    return True
                raise WrongAnswerException(f'{Q_S}\nshould be printed after answer')

    def test1_input1(self, out):
        if self.check_main_menu(out):
            return '1'

    def test1_input2(self, out):
        if self.check_sub_menu(out):
            return '1'

    def test1_input3(self, out):
        if self.check_question(out):
            return FIRST_QUESTION

    def test1_input4(self, out):
        if self.check_answer(out):
            return FIRST_ANSWER

    def test1_input5(self, out):
        if self.check_sub_menu(out):
            return '1'

    def test1_input6(self, out):
        if self.check_question(out):
            return SECOND_QUESTION

    def test1_input7(self, out):
        if self.check_answer(out):
            return SECOND_ANSWER

    def test1_input8(self, out):
        if self.check_sub_menu(out):
            return '2'

    def test1_input9(self, out):
        if self.check_main_menu(out):
            return '2'

    def test1_input10(self, out):
        if self.check_practice_question(out, FIRST_QUESTION):
            return 'y'

    def test1_input11(self, out):
        question = out.strip().split('\n')
        if len(question) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            question = '\n'.join(question)
            if self.check_practice_question(question.strip(), SECOND_QUESTION):
                return 'n'

    def test1_input12(self, out):
        if self.check_main_menu(out.strip()):
            return '3'

    def check(self, reply: str, attach):
        all_output = reply.strip().split('\n')
        if not 'Bye!' == all_output[-1]:
            raise WrongAnswerException('Bye! is missing or misspelling!')
        return CheckResult.correct()

    def test2_input1(self, out):
        if self.check_main_menu(out):
            return '5'

    def test2_input2(self, out):
        out_list = out.strip().split('\n')
        if len(out_list) < 2:
            raise WrongAnswerException("The output is not printed correctly")
        else:
            if not out_list[0] == '5 is not an option':
                raise WrongAnswerException('5 is not an option\nshould be printed in output')
            out_list.pop(0)
            if self.check_main_menu('\n'.join(out_list)):
                return 'we'

    def test2_input3(self, out):
        out_list = out.strip().split('\n')
        if len(out_list) < 2:
            raise WrongAnswerException("The output is not printed correctly")
        else:
            if not out_list[0] == 'we is not an option':
                raise WrongAnswerException('we is not an option\nshould be printed')
            out_list.pop(0)
            if self.check_main_menu('\n'.join(out_list)):
                return CheckResult.correct()

    def test3_input1(self, out):
        out_list = out.strip().split('\n')
        if len(out_list) < 2:
            raise WrongAnswerException("The output is not printed correctly")
        else:
            if not out_list[0] == '4 is not an option':
                raise WrongAnswerException('4 is not an option\nshould be printed')
            out_list.pop(0)
            if self.check_sub_menu('\n'.join(out_list)):
                return 'Rome'

    def test3_input2(self, out):
        out_list = out.strip().split('\n')
        if len(out_list) < 2:
            raise WrongAnswerException("The output is not printed correctly")
        else:
            if not out_list[0] == 'Rome is not an option':
                raise WrongAnswerException('Rome is not an option\nshould be printed')
            out_list.pop(0)
            if self.check_sub_menu('\n'.join(out_list)):
                return CheckResult.correct()

    def test4_input4(self, out):
        output = out.strip().split('\n')
        if not 'Question:' in output:
            raise WrongAnswerException("the question can't be empty!")
        return ''

    def test4_input5(self, out):
        output = out.strip().split('\n')
        if not 'Question:' in output:
            raise WrongAnswerException("the question can't be empty!")
        return CheckResult.correct()

    def test5_input5(self, out):
        output = out.strip().split('\n')
        if not 'Answer:' in output:
            raise WrongAnswerException("the answer can't be empty!")
        return ''

    def test5_input6(self, out):
        output = out.strip().split('\n')
        if not 'Answer:' in output:
            raise WrongAnswerException("the answer can't be empty!")
        return CheckResult.correct()

    def test7_input3(self, out):
        out_put_list = out.strip().split('\n')
        update_menu_list = UPDATE_MENU.strip().split('\n')
        if len(out_put_list) > 3 or len(out_put_list) < 2:
            raise WrongAnswerException(f'The update_menu has "2" lines and it should be like this: \n{UPDATE_MENU}')
        for index, content in enumerate(update_menu_list):
            if not content == out_put_list[index]:
                raise WrongAnswerException(f'The line no.{index + 1} should be like this: {content}')
        return 'd'

    def test7_input6(self, out):
        output_list = out.strip().split('\n')
        if len(output_list) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            first_line = output_list[0].split(':')
            if len(first_line) < 2:
                raise WrongAnswerException("The ':' is missing in output")
            else:
                second_line = output_list[1]
                if not first_line[0].strip() == "current question":
                    raise WrongAnswerException('current question\nis missing or misspelling')
                if not first_line[1].strip() == SECOND_QUESTION:
                    raise WrongAnswerException(' after current question: question should be printed')
                if not second_line == 'please write a new question:':
                    raise WrongAnswerException('please write a new question: \nis missing or misspelling')

        return NEW_SECOND_QUESTION

    def test7_input7(self, out):
        output_list = out.strip().split('\n')
        if len(output_list) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            first_line = output_list[0].split(':')
            if len(first_line) < 2:
                raise WrongAnswerException("The ':' is missing in output")
            else:
                second_line = output_list[1]
                if not first_line[0].strip() == "current answer":
                    raise WrongAnswerException('current answer:\nis missing or misspelling')
                if not first_line[1].strip() == SECOND_ANSWER:
                    raise WrongAnswerException(' after current answer: answer should be printed')
                if not second_line == 'please write a new answer:':
                    raise WrongAnswerException('please write a new answer: \nis missing or misspelling')
        return NEW_SECOND_ANSWER

    def test7_input8(self, out):
        if self.check_main_menu(out):
            return CheckResult.correct()

    def test8_input2(self, out):
        out_put_list = out.strip().split('\n')
        if len(out_put_list) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            first_line = out_put_list[0].strip().split(':')
            if not first_line[1].strip() == NEW_SECOND_QUESTION:
                raise WrongAnswerException("update function doesn't update question properly")

        return 'y'

    def test8_input3(self, out):
        out_put_list = out.strip().split('\n')
        if len(out_put_list) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            first_line = out_put_list[0].strip().split(':')
            if not first_line[1].strip() == NEW_SECOND_ANSWER:
                raise WrongAnswerException("update function doesn't update answer properly")

        return CheckResult.correct()

    def test9_input3(self, out):
        out_put_list = out.strip().split('\n')
        if len(out_put_list) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            first_line = out_put_list[0].strip().split(':')
            if len(first_line) < 2:
                raise WrongAnswerException("The ':' is missing in output")
            else:
                out_put_list.pop(0)
                check_learn_menu = '\n'.join(out_put_list)
                if not first_line[0].strip() == 'Answer':
                    raise WrongAnswerException('Answer is missing or misspelling')
                if not first_line[1].strip() == NEW_SECOND_ANSWER:
                    raise WrongAnswerException('before check_learn_menu the answer should be printed')
                if not check_learn_menu.strip() == CHECK_LEARN_MENU.strip():
                    raise WrongAnswerException(
                        f'your check_learn_menu:\n{check_learn_menu} \ncorrect check_learn_ menu\n'
                        f'{CHECK_LEARN_MENU} ')

        return CheckResult.correct()

    def test10_input11(self, out):
        out_put = out.strip().split('\n')
        if len(out_put) == 0:
            raise WrongAnswerException("The output can't be empty")
        else:
            first_line = out_put[0].strip()
            if not first_line == 'There is no flashcard to practice!':
                raise WrongAnswerException('After three successive correct answers the question should be deleted from '
                                           'database\nand the first line in the output should be like this:'
                                           ' \nThere is no flashcard to practice!')
        return CheckResult.correct()


if __name__ == '__main__':
    FlashCardTest().run_tests()
