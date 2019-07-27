import keyword

s1 = "elif"
s2 = "purushotham"

if(keyword.iskeyword(s1)):
    print(s1 + " is a python keyword ")
else:
    print(s1 + " is not a python keyword ")


if(keyword.iskeyword(s2)):
    print(s2 + " is a python keyword ")
else:
    print(s2 + " is not a python keyword ")
