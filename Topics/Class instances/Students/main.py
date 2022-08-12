class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here

    def student_id(self):
        print(f"{self.name[0]}{self.last_name}{self.birth_year}")
        hello()

    @classmethod
    def hello(cls):
        print("hello")


first_name = input()
surname = input()
date_birth = input()
Student.hello()
student = Student(first_name, surname, date_birth)
student.student_id()
