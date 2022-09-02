## Tutorial
### Workbook
- Create
` import openpyxl `
` wb = Workbook() `
- Query
` print(wb.sheetnames) ` # show all names of sheets

``` python
for sheet in wb:
	print(sheet.title)   # like abobe
```
- Copy

``` Python
  ws = wb.active
  ws_cp = wb.copy_worksheet(source)
```
	- Only cells (including values, styles, hyperlinks and comments) and certain worksheet attribues (including dimensions, format and properties) are copied. All other workbook / worksheet attributes are not copied - e.g. Images, Charts.
	- You also cannot copy worksheets between workbooks. You cannot copy a worksheet if the workbook is open in read-only or write-only mode.




### Sheet
- Activate
` ws = wb.active ` # activate the last active sheet
` ws2 = wb['sheet2'] ` # acitvate the sheet named 'sheet2'

- Create
` ws1 = wb.create_sheet('mysheet') ` # insert to the end; by the second para, we can set the position of the sheet. 0 means the first position; -1 means the penultimate position （倒数第二）
- Change Title (Rename)
` ws.title = 'New Title' ` # Change 'Sheet' --> 'New Title'

- Change Backgroud Color
` ws.sheet_properities.tabColor = "1072BA" ` # we need providing an `RRGGBB` color code

### Cell

