class Student:
    def __init__(self, name, roll, result):
        self.name = name
        self.roll = roll
        self.result = result

    def __repr__(self):
        return f'Name: {self.name} | Roll: {self.roll} | Result: {self.result}'

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, name, roll, result):
        student = Student(name, roll, result)
        cls.student_list.append(student)

StudentDatabase.add_student('koba', 10, 'A+')
StudentDatabase.add_student('sik', 9, 'A+')
StudentDatabase.add_student('der', 10, 'B+')
StudentDatabase.add_student('swarup', 11, 'A')
StudentDatabase.add_student('Ritu', 10, 'A-')



# Output
for student in StudentDatabase.student_list:
    print(student)