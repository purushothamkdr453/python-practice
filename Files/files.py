#--- file object attributes

fo = open("students.txt","wb")

print("File name : ", fo.name ) #-- Filename
print("File mode : ", fo.mode ) #-- file mode
print("File closed or not : ", fo.closed ) #-- file closed or not

print("purushotham")

fo.close() #-- closing the file

print("File closed or not : ", fo.closed )

#--- Writing to file

fo = open("students.txt","w")

fo.write("Purushotham")

fo.close()

#--- reading from file

fo = open("students.txt","r")

st = fo.read(4)
print(st)

current_position = fo.tell()
print(current_position)

change_position_from_current = fo.seek(0,1) #-- 1 indicates from the current position
print(fo.read(3))

change_position = fo.seek(0,0) #-- file pointer to the beginning
print(fo.tell())

#--- appending to the existing file

fo = open("students.txt","a")
fo.write("Chandra")
fo.close()
