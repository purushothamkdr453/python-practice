import calendar

#---------------- Iterweek days----------------------
obj = calendar.Calendar(firstweekday=2)

for day in obj.iterweekdays():
    print(day)

#----------------Itermonthdates----------------------------

obj=calendar.Calendar()
for day in obj.itermonthdates(2019,8):
    print(day)

print("-----------------------------------")

obj=calendar.Calendar(firstweekday=2)

for day in obj.itermonthdates(2019,8):
    print(day)

print("-----------------------------------------")
#---------itermonthdays----------------------------

obj = calendar.Calendar()

for day in obj.itermonthdays(2019,8):
    print(day)

print("-----------------------------------------")

obj = calendar.Calendar(firstweekday=3)

for day in obj.itermonthdays(2019,8):
    print(day)

print("-----------------------------------")
#---------itermonthdays2----------------------------

obj = calendar.Calendar()

for day in obj.itermonthdays2(2019,8):
    print(day)

print("-----------------------------------")

obj = calendar.Calendar(firstweekday=3)

for day in obj.itermonthdays2(2019,8):
    print(day)

print("-----------------------------------")

#--------------------- monthdatescalendar-------------------------

obj = calendar.Calendar()

for day in obj.monthdatescalendar(2019,8):
    print(day)

print("------------------------------------")

#-------------------- monthdays2calender-------------

obj = calendar.Calendar()

for day in obj.monthdays2calendar(2019,8):
    print(day)

print("------------------------------------")

#-------------------- monthdayscalender-------------

obj = calendar.Calendar()

for day in obj.monthdayscalendar(2019,8):
    print(day)

print("------------------------------------")

#------------------- yeardayscalendar------------

obj = calendar.Calendar()

for day in obj.yeardayscalendar(2019,1):
    print(day)

print("------------------------------------")

#-------------------- yeardays2calendar--------------

obj = calendar.Calendar()

for day in obj.yeardays2calendar(2019,1):
    print(day)

print("------------------------------------")

#----------------------yeardatescalendar------------

obj = calendar.Calendar()

for day in obj.yeardatescalendar(2019,1):
    print(day)