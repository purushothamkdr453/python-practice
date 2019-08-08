a=5
b=2



try:
    print("file opened")
    print(a/b)
    n = int(input("Enter the value"))
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
finally:
    print("file closed")

print("Bye")