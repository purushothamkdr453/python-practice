students = []

class Student:
    school_name = "Manikanta Vidyanikethan" # Class Attrbute
    def __init__(self,name,student_id='100'):
        self.name = name
        self.student_id = student_id
        students.append(self)
        
    def __str__(self):
        return "student - " + self.name
    
    def get_name_capitalize(self):
        return self.name.upper()

    def get_school_name(self):
        return self.school_name

student = Student("Purushotham")
print(students)
print(student)
print(student.get_name_capitalize())
print(student.get_school_name())
print(Student.school_name)
