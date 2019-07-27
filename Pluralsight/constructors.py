students = []

class Student:
    def __init__(self, name, student_id='100'): # constructor method
        student = { "name": name, "studentid": student_id }
        students.append(student)
    def __str__(self): #override method called during printing the instance class
        return "student"

mark = Student("Chandra")
print(mark)
#print(students)
        

