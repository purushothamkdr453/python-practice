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

#print(os.getcwd())

#-- Deleting the directory

#os.rmdir("students")

#--- Listing .txt files in specific directory & subdirectories
"""
path = 'C:\\purushotham\\Learning\\python-learning'

files = []

for r,d,f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r,file))

for i in files:
    print(i)
    """

#---- Listing directories in specific directory & sub-directory

path = 'C:\\purushotham\\Learning\\python-learning'

folders = []
#--- r=root,d=directory,f=file
for r,d,f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r,folder))

for folder in folders:
    print(folder)


