import openpyxl
from openpyxl.chart import BarChart3D,Reference

wb = openpyxl.Workbook()

sheet = wb.active

for i in range(10):
    sheet.append([i])

values = Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)

chart = BarChart3D()

chart.add_data(values)

chart.title = " Bar-Chart 3D "
chart.x_axis.title = " X_Axis"
chart.y_axis.title = " Y_Axis"

sheet.add_chart(chart,'E2')

wb.save("barchart3d.xlsx")
