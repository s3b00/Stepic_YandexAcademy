import xlrd

wb = xlrd.open_workbook("trekking2.xlsx")
sh = wb.sheet_names()
table = wb.sheet_by_name(sh[0])

names = table.col_values(0, 1)
cals = {}
for x in range(1, len(names)):
    cals[names[x - 1]] = table.col_values(1, x, end_rowx=x + 1)[0]

for r in sorted(cals.items(), key=lambda x: (-x[1], x[0])):
    print(r[0])
