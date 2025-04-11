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

    # To Access the private id
    def get_id(self):
        return self.__student_id

    def drop_student(self):
        if self.__is_enrolled == True:
            self.__is_enrolled = False
            
            # modify the is_enrolled to false for student
        else:
            print(f"{self.name} is already dropped out.")


    def __repr__(self):
        return f'ID: {self.__student_id}, Name: {self.name}, Dept: {self.__department}, Enrolled: {self.__is_enrolled}'
    

class StudentDatabase:
    student_list = [
        Student(100, 'ALif', 'IPE', True),
        Student(101, 'Kopa', 'CSE', True),
        Student(102, '', 'EEE', False),
        Student(103, 'Sikder', 'CSE', True)
    ]

    def get_student_by_ID(self, id):
        for student in self.student_list:
            if id == student.get_id():
                return student
            
        return None


    

    


famousSchool = StudentDatabase()
student = famousSchool.get_student_by_ID(103)
if student:
    student.drop_student()




# output
for student in famousSchool.student_list:
    print(student)
