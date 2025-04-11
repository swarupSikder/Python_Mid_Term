class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def enroll_student(self, student):
        if self.__is_enrolled == False:
            self.__is_enrolled = True           # it will change id:104 (False -> True)
            
            database = StudentDatabase()
            database.student_list.append(student)
        else:
            print(f"{self.name} is already enrolled.")

    def __repr__(self):
        return f'ID: {self.__student_id}, Name: {self.name}, Dept: {self.__department}, Enrolled: {self.__is_enrolled}'
    

class StudentDatabase:
    student_list = [
        Student(100, 'ALif', 'IPE', True),
        Student(101, 'Kopa', 'CSE', True),
        Student(102, '', 'EEE', False),
        Student(103, 'Sikder', 'CSE', True)
    ]


    

    


famousSchool = StudentDatabase()
s1 = Student(104, 'Alan', 'EEE', False)
s1.enroll_student(s1)


# # output
for student in famousSchool.student_list:
    print(student)
