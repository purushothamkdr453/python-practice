import os

#--- renaming the files
#os.rename("students.txt","students_list.txt")

#-- removing the file

#os.remove("students_list.txt")

#-- creating directory

#os.mkdir("C:\purushotham\Learning\python-learning\Python-practice\os-module\students")

#-- changing to the different directory

#os.chdir("students")

#-- getting the current working directory

print(os.getcwd())

#-- Deleting the directory

os.rmdir("students")
