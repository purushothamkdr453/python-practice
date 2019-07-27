import openpyxl

wb = openpyxl.Workbook()

#--- Sum

sheet = wb.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 400
sheet['A4'] = 500
sheet['A5'] = 600

sheet['A7'] = '=SUM(A1:A5)'

wb.save("sum.xlsx")

#-- product

sheet['A1'] = 2
sheet['A2'] = 3
sheet['A3'] = 4
sheet['A4'] = 5
sheet['A5'] = 6

sheet['A7'] = '=PRODUCT(A1:A5)'

wb.save("product.xlsx")

#--- count

sheet['A1'] = 2
sheet['A2'] = 3
sheet['A3'] = 4
sheet['A4'] = 5
sheet['A5'] = 6
sheet['A7'] = '=COUNT(A1:A5)'

wb.save("count.xlsx")

#--- Modulation

sheet['A1']='=MOD(25,6)'
sheet['A2']='=MOD(24,6)'

wb.save("module.xlsx")

#--- quotient

sheet['A1']='=QUOTIENT(64,8)'
sheet['A2']='=QUOTIENT(25,4)'

wb.save("quotient.xlsx")

#--- average

sheet['A1']=10
sheet['A2']=20
sheet['A3']=30
sheet['A4']=40
sheet['A5']=50

sheet['A7']='=AVERAGE(A1:A5)'

wb.save("Average.xlsx")
