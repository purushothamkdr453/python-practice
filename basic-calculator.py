
print("Please select operations - \n" \
       "1. Addition \n" \
       "2. Subtraction \n" \
       "3. Multiply \n" \
       "4. Divide \n" )

operation = input("Please select the operaion - 1, 2, 3, 4 - ")
number_1 = int(input("Please enter number 1 - "))
number_2 = int(input("Please enter number 2 - "))

def Add(num1,num2):
    result = num1 + num2
    return result

def Subtract(num1,num2):
    result = num1 - num2
    return result

def Multiply(num1,num2):
    result = num1 * num2
    return result

def Divide(num1,num2):
    result = num1 * num2
    return result             

if operation == '1':
    print(number_1,"+",number_2,"=",Add(number_1,number_2))
elif operation == '2':
    print(number_1,"-",number_2,"=",Subtract(number_1,number_2))
elif operation == '3':
    print(number_1,"*",number_2,"=",Multiply(number_1,number_2))
elif operation == '4':
    print(number_1,"/",number_2,"=",Divide(number_1,number_2))
else:
    print("Invalid Input")



    
               
