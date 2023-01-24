from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date
from datetime import datetime, timedelta


class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///todo.db?check_same_thread_=False')
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        class Table(self.Base):
            __tablename__ = 'task'
            id = Column(Integer, primary_key=True)
            task = Column(String, default='task')
            deadline = Column(Date, default=datetime.today())

            def __repr__(self):
                return self.task

        self.Table = Table
        self.create_table()

    def create_table(self):
        self.Base.metadata.create_all(self.engine)


class App(Database):
    def task_today(self):
        print(datetime.today().strftime('%A %#d %b:'))
        rows = self.session.query(self.Table).filter(self.Table.deadline == datetime.today().date()).all()
        if rows:
            for i, j in enumerate(rows):
                print(f'{i + 1}) {j.task}')
        else:
            print('Nothing to do!')

    def task_week(self):
        for i in range(7):
            check = datetime.today().date() + timedelta(days=i)
            rows = self.session.query(self.Table).filter(self.Table.deadline == check).all()
            print(check.strftime('%A %#d %b:'))
            if rows:
                for p, j in enumerate(rows):
                    print(f'{p + 1}) {j.task}')
            else:
                print('Nothing to do!')
            print()

    def task_all(self):
        rows = self.session.query(self.Table).order_by(self.Table.deadline).all()
        if rows:
            for i, j in enumerate(rows):
                print(f'{i + 1}) {j.task}. {j.deadline.strftime("%#d %b")}')
        else:
            print('Nothing to do!')

    def task_missed(self):
        rows = self.session.query(self.Table).filter(self.Table.deadline < datetime.today().date()).all()
        print('Missed tasks:')
        if rows:
            for i, j in enumerate(rows):
                print(f'{i + 1}) {j.task}. {j.deadline.strftime("%#d %b")}')
            print()
        else:
            print('Nothing is missed!')

    def task_add(self):
        task = input("Enter task:")
        deadline = datetime.strptime(input("Enter deadline:"), '%Y-%m-%d')
        self.session.add(self.Table(task=task, deadline=deadline))
        self.session.commit()
        print('The task has been added!')

    def task_delete(self):
        rows = self.session.query(self.Table).order_by(self.Table.deadline).all()
        if rows:
            for i, j in enumerate(rows):
                print(f'{i + 1}) {j.task}. {j.deadline.strftime("%#d %b")}')
            dlt = int(input('Choose the number of the task you want to delete:'))
            dlt_row = rows[dlt - 1]
            self.session.delete(dlt_row)
            self.session.commit()
            print('The task has been deleted!')
        else:
            print('Nothing to delete')

    def run(self):
        while True:
            print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task
6) Delete a task
0) Exit""")
            choice = input()
            match choice:
                case '1':
                    self.task_today()
                case '2':
                    self.task_week()
                case '3':
                    self.task_all()
                case '4':
                    self.task_missed()
                case '5':
                    self.task_add()
                case '6':
                    self.task_delete()
                case '0':
                    exit("Bye!")


if __name__ == '__main__':
    App().run()
