import openpyxl
import csv

wb = openpyxl.load_workbook('SampleData.xlsx')

sheet_ls = []
for sheet in wb:
    sheet_ls.append(sheet.title)

# print(sheet_ls)

for sheet in sheet_ls:
    ws = wb[sheet]
    
    for row in ws.rows:
        data_ls = []
        for col in row:
            data_ls.append(str(col.value))
        col_data = ','.join(data_ls)
        print(col_data)
        print()
