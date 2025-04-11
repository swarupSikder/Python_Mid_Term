class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    @classmethod
    def add_student(cls, name, roll, result):
        student = Student(name, roll, result)
        cls.student_list.append(student)


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
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        return status

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"{self.get_name()} has been successfully enrolled.")
        else:
            print(f"{self.get_name()} is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.get_name()} has been dropped.")
        else:
            print(f"{self.get_name()} is not currently enrolled.")

    def view_student_info(self):
        print(f'ID: {self.get_id()}, Name: {self.get_name()}, Dept: {self.get_dept()}, Enrolled: {self.get_enrolled()}')

    def __repr__(self):
        return f'ID: {self.get_id()}, Name: {self.get_name()}, Dept: {self.get_dept()}, Enrolled: {self.get_enrolled()}'

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

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


    

#---Manually added students---
StudentDatabase.add_student(Student(100, "Alif", "IPE", True))
StudentDatabase.add_student(Student(101, "kopa", "CSE", False))
StudentDatabase.add_student(Student(102, "samsu", "IPE", True))
StudentDatabase.add_student(Student(103, "sikder", "IPE", True))


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
        if not (100 <= st_id < 201):
            print('Invalid student ID')
            continue

        if famousSchool.get_student_by_ID(st_id):
            print("A student with this ID already exists.")
            continue


        st_name = input('Enter Student Name: ')
        st_dept = input('Enter department: ')
        newStudent = Student(st_id, st_name, st_dept, True)

        if newStudent.get_id() > 99 and newStudent.get_id() < 201:
            newStudent.enroll_student()
            # famousSchool.view_all_students()
        else:
            print('Invalid student ID')
    elif opt == '3':
        st_id = int(input('Enter a valid Student ID: '))

        student = famousSchool.get_student_by_ID(st_id)
        if student and 99 < student.get_id() < 201:
            student.drop_student()
            # famousSchool.view_all_students()
        else:
            print('Invalid student ID')
    elif opt == '4':
        print('Exit Done...')
        break
    else:
        print('Invalid option. Try again!')
