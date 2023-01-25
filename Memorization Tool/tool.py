from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        class Table(self.Base):
            __tablename__ = 'flashcard'
            id = Column(Integer, primary_key=True)
            question = Column(String)
            answer = Column(String)
            box = Column(Integer)

        self.Table = Table
        self.create_table()

    def create_table(self):
        self.Base.metadata.create_all(self.engine)


class Flashcard(Database):
    def new(self):
        while True:
            question = input('Question:')
            if question.strip():
                break

        while True:
            answer = input('Answer:')
            if answer.strip():
                self.session.add(self.Table(question=question, answer=answer, box=1))
                self.session.commit()
                break

    def practice(self):
        flashcards = [[flashcard.question, flashcard.answer, flashcard.box] for flashcard in self.session.query(self.Table).all()]
        if len(flashcards) == 0:
            print('There is no flashcard to practice!')
            return

        for pair in flashcards:
            print(f'Question: {pair[0]}')
            while True:
                print('press "y" to see the answer:\n'
                      'press "n" to skip:\n'
                      'press "u" to update:')
                option = input()
                if option == 'y':
                    print(f'Answer: {pair[1]}')
                    self.check(pair)
                    break

                elif option == 'n':
                    break

                elif option == 'u':
                    self.update(pair)
                    break

                else:
                    print(f'{option} is not an option')

    def check(self, pair):
        while True:
            print('press "y" if your answer is correct:\n'
                  'press "n" if your answer is wrong:')
            option = input()
            if option == 'y':
                self.rank(pair, 'y')
                break

            elif option == 'n':
                self.rank(pair, 'n')
                break

            else:
                print(f'{option} is not an option')

    def rank(self, pair, correctness):
        flashcard = self.session.query(self.Table).filter(self.Table.question == pair[0])[0]
        flashcard.box = flashcard.box + 1 if correctness == 'y' else 1
        self.session.commit()

        if flashcard.box == 3:
            self.session.delete(self.session.query(self.Table).filter(self.Table.question == pair[0])[0])

    def update(self, pair):
        while True:
            print('press "d" to delete the flashcard:\n'
                  'press "e" to edit the flashcard:')
            option = input()
            if option == 'd':
                self.session.delete(self.session.query(self.Table).filter(self.Table.question == pair[0])[0])
                break

            elif option == 'e':
                self.edit(pair)
                break

            else:
                print(f'{option} is not an option')

    def edit(self, pair):
        print(f'current question: {pair[0]}')
        new_question = input('please write a new question:')
        if not new_question.strip():
            new_question = pair[0]

        print(f'current answer: {pair[1]}')
        new_answer = input('please write a new answer:')
        if not new_answer.strip():
            new_answer = pair[1]

        flashcard = self.session.query(self.Table).filter(self.Table.question == pair[0])[0]
        flashcard.question = new_question
        flashcard.answer = new_answer
        flashcard.box = 1
        self.session.commit()

    def main(self):
        while True:
            print('1. Add flashcards\n'
                  '2. Practice flashcards\n'
                  '3. Exit')
            choice = input()
            if choice == '1':
                while True:
                    print('1. Add a new flashcard\n'
                          '2. Exit')
                    option = input()
                    if option == '1':
                        self.new()
                    elif option == '2':
                        break
                    else:
                        print(f'{option} is not an option')

            elif choice == '2':
                self.practice()

            elif choice == '3':
                print('Bye!')
                break

            else:
                print(f"{choice} is not an option")


if __name__ == '__main__':
    Flashcard().main()
