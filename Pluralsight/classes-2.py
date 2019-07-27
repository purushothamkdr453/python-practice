students = []
class Student:
    def addstudent(self, name, student_id='332'):
        student = { "name": name, "student_id": student_id }
        students.append(student)

student = Student()
student.addstudent("Chandra")
print(students)
        
