class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def __repr__(self):
        return f'ID: {self.student_id}, Name: {self.name}, Dept: {self.department}, Enrolled: {self.is_enrolled}'
    


student_1 = Student(101, 'Kopa', 'CSE', True)
student_2 = Student(102, 'Samsu', 'EEE', False)

print(student_1)
print(student_2)
