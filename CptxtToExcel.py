#! python 
# CptxtToExcel.py 

import openpyxl,os

wb = openpyxl.Workbook()
sheet = wb.active
columnNum = 0


for filename in os.listdir():
	if filename.endswith('.txt'):
		tempfile = open(filename)
		rowNum = 0
		columnNum +=1
		for word in tempfile.readlines():
			rowNum +=1
			sheet.cell(row = rowNum,column = columnNum).value = word

wb.save("CptxtToExcel.xlsx")
