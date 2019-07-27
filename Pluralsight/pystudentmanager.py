students = []

def get_students_list_title():
    student_title_case = []
    for student in students:
        student_title_case.append(student["name"].title())
    return student_title_case

def print_students_list_title():
    student_title_case=get_students_list_title()
    print(student_title_case)

def addstudent(name,student_id=30):
    student={"name": name, "studentid": student_id}
    students.append(student)

def savefile(student):
    try:
        f = open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not write to file")

def readfile():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            addstudent(student)
        f.close()
    except Exception:
        print("could not read file")

readfile()
print_students_list_title()
    
student_name = input("Please enter student name : ")
student_id = input("Please enter student id : ")

addstudent(student_name, student_id)
savefile(student_name)

