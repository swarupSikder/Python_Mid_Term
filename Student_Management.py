class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def __repr__(self):
        return f'ID: {self.student_id}, Name: {self.name}, Dept: {self.department}, Enrolled: {self.is_enrolled}'
    

class StudentDatabase:
    student_list = []

    def add_student(self, student):
        self.student_list.append(student)
        

famousSchool = StudentDatabase()
student_1 = Student(101, 'Kopa', 'CSE', True)
student_2 = Student(102, 'Samsu', 'EEE', False)

famousSchool.add_student(student_1)
famousSchool.add_student(student_2)



# output
for student in famousSchool.student_list:
    print(student)
