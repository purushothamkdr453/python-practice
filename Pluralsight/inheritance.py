students = []
class Student:
    
    school_name = "Manikanta school"
    
    def __init__(self, name, student_id='100'):
        self.name=name
        self.student_id=student_id
        students.append(self)
    def __str__(self):
        return "Student - " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class Highschoolstudent(Student):
    school_name = "Vignan High school"

    def get_name_capitalize(self):
        originalvalue = super().get_name_capitalize()
        return originalvalue + "-HS"

purushotham = Highschoolstudent("purushotham")
print(purushotham.get_name_capitalize())

print(purushotham.school_name)
