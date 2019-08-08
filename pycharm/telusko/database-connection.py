import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='purushotham',passwd='1234',database='telusko')

mycursor = mydb.cursor()

mycursor.execute("select * from students")

#------ fetchall

#result = mycursor.fetchall()

#for i in result:
    #print(i)

#-------fetchone

singleres = mycursor.fetchone()
print(singleres)

#----------- fetching the data from cursor
#for j in mycursor:
    #print(j)


