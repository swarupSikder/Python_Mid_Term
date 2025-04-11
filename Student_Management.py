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


    def view_student_info(self):
        print(f'ID: {self.__student_id}, Name: {self.name}, Dept: {self.__department}, Enrolled: {self.__is_enrolled}')


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
    
    
    def view_all_students(self):
        if not self.student_list:
            print("No students found")
        else:
            for student in self.student_list:
                print(student)


    

    


famousSchool = StudentDatabase()
while True:
    print('\n1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    opt = input("Enter your option (1-4): ")
    if opt == '1':
        famousSchool.view_all_students()
    elif opt == '2':
        newStudent = Student(104, 'Alan', 'EEE', False)
        newStudent.enroll_student(newStudent)
    elif opt == '3':
        student = famousSchool.get_student_by_ID(104)
        if student:
            student.drop_student()
    elif opt == '4':
        print('Exit Done...')
        break
    else:
        print('Invalid option. Try again!')
