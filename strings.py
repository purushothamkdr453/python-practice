#- creating a string with single quotes

print('Hello puruhsotham')

#-- creating a string with double quotes

print("I'm Purushotham")

#-- creating a string with triple quotes

print('''I'm "purushotham"''')

#-- creating a string that allows to take multiple line strings

print('''Hello
Purushotham
Reddy''')

#--- Accessing the characters of the strings

message="hello world"

print(message)

print(message[1])

#message[1]='p' # string object does not support item assignment

print(message[0:5])

print(message[3:-1])

#-- updating entire string is possible

string1 = "hello"
print(string1)
string1 = "hey"
print(string1)

#-- deleting single character/item of string is not possible

#del(string1[0])

#-- Deleting entire string is possible

del string1
#print(string1)

#--Escape characters are used for special meaning

print('''I'm "Purushotham"''')
print('I\'m Purushotham')
print("I am \"Purushotham\"")
print("\x47")

#-- to ignore special meanig i.e '\' you can use r or R

print(r"\x47")

# python string formatting

# default order

print("{}{}{}".format("Hello","purushotham","reddy"))
print("{1}{0}{2}".format("Hello","purushotham","reddy"))
print("{caste}{name}{wish}".format(wish="Hello",name="purushotham",caste="reddy"))

# rounding of integers

print("{0:.2f}".format(1/6))

# string alignment

print("|{:<10}|{:^10}|{:>10}|".format("hello","purushotham","reddy"))


integer1 = 12.3456789
print("value is %3.2f" %(integer1))
print("value is %3.4f" %(integer1))

