students = []

def readfile():
    try:
        f = open("students.txt","r")
        for student in reading_lines(f):
            students.append(student)
        f.close()
    except Exception:
        print("could not read file")

def reading_lines(f):
    for line in f:
        yield line
    
readfile()
print(students)
