import glob

#---- in the path variable mentioned below if u include trailling slashes \\ i.e after python-learning then it will check sub-directories

#--- checking the .txt files in current directory

"""
path = 'C:\\purushotham\\Learning\\python-learning'

files = [ f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)
"""


#------ checking the .txt files in both current & sub-directory

"""
path = 'C:\\purushotham\\Learning\\python-learning\\'

files = [ f for f in glob.glob(path+"**/*.txt",recursive=True)]

for i in files:
    print(i)
    """

#------- checking the directories in both current & sub-directory

path = 'C:\\purushotham\\Learning\\python-learning\\'

dirs = [ d for d in glob.glob(path+"**/",recursive=True)]

for d in dirs:
    print(d)


