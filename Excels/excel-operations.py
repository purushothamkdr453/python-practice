import xlrd

loc=("C:\purushotham\Learning\python-learning\Python-practice\Excels\students.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print((sheet.cell_value(0,0)))

#-- Printing the number of columns

print("Number of columns are : " ,sheet.ncols)

#--- Printing the number of rows

print("Number of rows are : ", sheet.nrows)

#--- extracting the column names

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))

#--- Extracting the first column details

for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))

#--- extracing the row values

print(sheet.row_values(2))

import xlwt

#---- writing the content to file

#wb = xlwt.Workbook()

#sheet=wb.add_sheet("sheet")

#sheet.write(0,0,"Hello")
#wb.save("wish.xls")

#-- adding styles to the text

#wb = xlwt.Workbook()
#sheet = wb.add_sheet("first")
#style = xlwt.easyxf('font: Bold 1')
#sheet.write(0,0,"hello",style)
#wb.save("wish.xls")

#-- adding multiple styles

wb = xlwt.Workbook()
sheet = wb.add_sheet("first")
style = xlwt.easyxf('font: bold 1, color red;')
sheet.write(0,0,"Hello",style)
wb.save("wish.xls")

