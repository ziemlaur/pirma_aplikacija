# import openpyxl
# import os
# wb = openpyxl.load_workbook('lenteliukas.xlsx')
# print(wb.sheetnames)
# sheet = wb['Sheet3']
# print(sheet)
# print(sheet.title)
# anotherSheet = wb.active
# print(anotherSheet)
# c=sheet['C1']
# print('Row %s, Column %s is %s' % (c.row, c.column, c.value))

# from openpyxl.utils import get_column_letter, column_index_from_string
# print(get_column_letter(3))
# print(column_index_from_string('A'))



# from openpyxl.comments import Comment
# from openpyxl.drawing.image import Image
# wb = openpyxl.load_workbook('lenteliukas.xlsx')
# print(wb)
# sheet = wb.active
# sheet = wb['Sheet1']
# cell=sheet['A1']
# comm = Comment('komentaras')
# comm = sheet ['A1'].comment
# img=Image
# #Klausimai
#1. What does the openpyxl.load_workbook() function return?
#openpyxl.workbook.workbook.Workbook object

# 2. What does the wb.sheetnames workbook attribute contain?
#  list of all sheet names in the workbook

# 3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?

# sheet = wb['Sheet1']
# 4. How would you retrieve the Worksheet object for the workbook’s active sheet?

# sheet = wb.active
# 5. How would you retrieve the value in the cell C5?

# value = sheet['C5'].value
# 6. How would you set the value in the cell C5 to "Hello"?

# sheet['C5'].value = "Hello"
# 7. How would you retrieve the cell’s row and column as integers?

# cell = sheet['C5']
# row = cell.row 
# column = cell.column
# 8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?

# maximum number of columns
# maximum number of rows 
# Int.

# 9. If you needed to get the integer index for column 'M', what function would you need to call?

# from openpyxl.utils import column_index_from_string
# index = column_index_from_string('M')
# 10. If you needed to get the string name for column 14, what function would you need to call?

# from openpyxl.utils import get_column_letter
# column = get_column_letter(14)
# 11. How can you retrieve a tuple of all the Cell objects from A1 to F1?

# cells = tuple(sheet['A1':'F1'])
# 12. How would you save the workbook to the filename example.xlsx?

# wb.save('example.xlsx')
# 13. How do you set a formula in a cell?

# sheet['C5'].value = "=SUM(A1:A10)"
# 14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?

# wb = openpyxl.load_workbook('example.xlsx', data_only=True)
# 15. How would you set the height of row 5 to 100?

# sheet.row_dimensions[5].height = 100
# 16. How would you hide column C?
# sheet.column_dimensions['C'].hidden = True
# 17. What is a freeze pane?

# Locks certain rows or columns in place so that they remain visible when scrolling
# 18. What five functions and methods do you have to call to create a bar chart?

# from openpyxl.chart import BarChart, Reference
# chart = BarChart()
# data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=10)
# chart.add_data(data, titles_from_data=True)
# sheet.add_chart(chart, 'E5')


# 1.	Write a program that reads an Excel file and prints the values of the first column.
# import openpyxl
# wb = openpyxl.load_workbook('lentele.xlsx')
# sheet = wb.active 

# for i in range(1, sheet.max_row + 1):
#     print(i, sheet.cell(row=i, column=1).value)

# 2.	Create an Excel file and write random sales data to it. 
# import openpyxl

# workbook = openpyxl.Workbook()
# sheet = workbook.active

# sales_data = [
#     ['Salesperson', 'Region', 'Sales Amount'],
#     ['Alice', 'North', 1500],
#     ['Bob', 'South', 2500],
#     ['Charlie', 'East', 3000]
# ]

# for i in sales_data:
#     sheet.append(i)

# workbook.save('sales_data.xlsx')
 
# 3.	Write a script that adds a formula to an Excel sheet to calculate the sum of a column of numbers. 

# import openpyxl

# workbook = openpyxl.Workbook()
# sheet = workbook.active

# numbers = [10, 20, 30, 40, 50]
# for i, number in enumerate(numbers, start=1):
#     sheet.cell(row=i, column=1, value=number)

# sheet['A6'] = '=SUM(A1:A5)' 

# workbook.save('sum.xlsx')

# 4.	Generate a chart in Excel using sales data and save the file.  

# import openpyxl
# from openpyxl.chart import BarChart, Reference

# workbook = openpyxl.Workbook()
# sheet = workbook.active

# sheet.append(['Salesperson', 'Sales Amount']) 

# sales_data = [
#     ['Alice', 1500],
#     ['Bob', 2000],
#     ['Charlie', 2500],
#     ['David', 3000],
#     ['Eva', 3500]
# ]

# for row in sales_data:
#     sheet.append(row)

# chart = BarChart()
# chart.title = "Sales Data"
# chart.x_axis.title = "Salesperson"
# chart.y_axis.title = "Sales Amount"


# data = Reference(sheet, min_col=2, min_row=1, max_row=len(sales_data)+1)
# categories = Reference(sheet, min_col=1, min_row=2, max_row=len(sales_data)+1)


# chart.add_data(data, titles_from_data=True)
# chart.set_categories(categories)


# sheet.add_chart(chart, "D4") 


# workbook.save('sales_data_chart_simple.xlsx')

# print('Excel file with sales data and chart has been created: sales_data_chart_simple.xlsx')