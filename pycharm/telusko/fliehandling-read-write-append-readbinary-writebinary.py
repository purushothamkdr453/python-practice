#---- Commented codes to

#----- read mode
f=open('sample.txt','r')
#--- printing single line
#print(f.readline(),end="")
#---- Printing all the content
#for i in f:
    #print(i,end="")
#--------- Write mode
#w=open('output.txt','w')
#for i in f:
    #w.write(i)
#---- Apending mode
#a=open('output.txt','a')
#a.write("This is appended text")
#a.close()
#---- read binary------------
p = open('purushotham.jpg','rb')
#for i in p:
    #print(i)
#---- Write binary------------
w = open('mypic.jpg','wb')

for i in p:
    w.write(i)
