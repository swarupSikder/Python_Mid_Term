#   -   -   -   -   -   #
#                       #
#       Student DB      #
#                       #
#   -   -   -   -   -   #
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
        print('\n---------------------------')
        print('|       Student List      |')
        print('---------------------------\n')
        print('ID\tName\tDept\tEnroll_Status')

        if not self.student_list:
            print("-\t-\t-\t-")
        else:
            for student in self.student_list:
                student.view_student_info()









#   -   -   -   -   -   #
#                       #
#        Student        #
#                       #
#   -   -   -   -   -   #
class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

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
        if self.__is_enrolled:
            return True
        else:
            return False

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"[x] {self.get_name()} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"{self.get_name()} has been successfully enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.get_name()} has been dropped.")
        else:
            print(f"[x] {self.get_name()} is not currently enrolled.")

    def view_student_info(self):
        print(f'{self.get_id()}\t{self.get_name()}\t{self.get_dept()}\t{self.get_enrolled()}')



    




#   -   -   -   -   -   #
#        Manually       #
#         Added         #
#        Students       #
#   -   -   -   -   -   #
StudentDatabase.add_student(Student(100, "Alif", "IPE", True))
StudentDatabase.add_student(Student(101, "kopa", "CSE", False))
StudentDatabase.add_student(Student(102, "samsu", "IPE", True))
StudentDatabase.add_student(Student(103, "sikder", "IPE", True))

menuText = """
---------------------------------
|    Student Management Menu    |
---------------------------------
1. View All Students
2. Enroll Student
3. Drop Student
4. Exit

"""












#   -   -   -   -   -   #
#          Main         #
#         [Menu]        #
#          Task         #
#   -   -   -   -   -   #
famousSchool = StudentDatabase()
while True:
    print(menuText)
    opt = input("Enter your option (1-4): ")


    #   -   -   -   -   -   #
    #   View All Students   #
    #   -   -   -   -   -   #
    if opt == '1':
        famousSchool.view_all_students()

    #   -   -   -   -   -   #
    #    Enroll Students    #
    #   -   -   -   -   -   #
    elif opt == '2':
        print('\n---------------------------')
        print('|      Enroll Student     |')
        print('---------------------------\n')
        try:
            st_id = input('Enter Student ID: ')
            student = famousSchool.get_student_by_ID(int(st_id))
            if student:
                if student.get_enrolled():
                    print(f'[x] {student.get_name()} is already enrolled.')
                else:
                    student.enroll_student()
            else:
                print(f'[x] Student with ID-[{st_id}] is not found!')

        except ValueError:
            print('[x] Invalid Input! Please try again...')


    #   -   -   -   -   -   #
    #      Drop Student     #
    #   -   -   -   -   -   #
    elif opt == '3':
        print('\n---------------------------')
        print('|      Drop A Student     |')
        print('---------------------------\n')
        try:
            st_id = input('Enter Student ID: ')
            student = famousSchool.get_student_by_ID(int(st_id))
            if student:
                student.drop_student()
            else:
                print(f'[x] Student with ID-[{st_id}] is not found!')

        except ValueError:
            print('[x] Invalid Input! Please try again...')


    #   -   -   -   -   -   #
    #          Exit         #
    #   -   -   -   -   -   #
    elif opt == '4':
        print('Exit Done...')
        break
    else:
        print('[x] Invalid option. Try again!')
