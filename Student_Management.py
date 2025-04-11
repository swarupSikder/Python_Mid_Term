class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def enroll_student(self, student):
        if self.__is_enrolled == False:
            self.__is_enrolled = True           # it will change id:104 (False -> True)
            
            database = StudentDatabase()
            database.student_list.append(student)
        else:
            print(f'Trying to enroll {self.get_name()} who is already enrolled')

    # To Access the private id
    def get_id(self):
        return self.__student_id
    
    # To Access the private name
    def get_name(self):
        return self.__name
    
    # To Access the private department
    def get_dept(self):
        return self.__department
    
    # To Access the private enrolled
    def get_enrolled(self):
        return self.__is_enrolled

    def drop_student(self):
        if self.__is_enrolled == True:
            self.__is_enrolled = False
            
            # modify the is_enrolled to false for student
        else:
            print(f'Trying to drop {self.get_name()} who is not enrolled')


    def view_student_info(self):
        print(f'ID: {self.get_id()}, Name: {self.get_name()}, Dept: {self.get_dept()}, Enrolled: {self.get_enrolled()}')


    def __repr__(self):
        return f'ID: {self.get_id()}, Name: {self.get_name()}, Dept: {self.get_dept()}, Enrolled: {self.get_enrolled()}'
    

class StudentDatabase:
    student_list = [
        Student(100, 'Alif', 'IPE', True),
        Student(101, 'Kopa', 'CSE', True),
        Student(102, 'Samsu', 'EEE', False),
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
    print('\n----Student Management Menu----')
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    opt = input("Enter your option (1-4): ")
    if opt == '1':
        famousSchool.view_all_students()
    elif opt == '2':
        st_id = int(input('Enter a valid Student ID: '))
        st_name = input('Enter Student Name: ')
        st_dept = input('Enter department: ')
        st_enrolled = input('Enter enrollment status: ')
        newStudent = Student(st_id, st_name, st_dept, st_enrolled)

        if newStudent.get_id() > 99 and newStudent.get_id() < 201:
            newStudent.enroll_student(newStudent)
            famousSchool.view_all_students()
        else:
            print('Invalid student ID')
    elif opt == '3':
        st_id = int(input('Enter a valid Student ID: '))

        student = famousSchool.get_student_by_ID(st_id)
        if student and newStudent.get_id() > 99 and newStudent.get_id() < 201:
            student.drop_student()
            famousSchool.view_all_students()
        else:
            print('Invalid student ID')
    elif opt == '4':
        print('Exit Done...')
        break
    else:
        print('Invalid option. Try again!')
