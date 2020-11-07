import xlrd

wb = xlrd.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

cities = []
for i in range(1, 9):
    tmp = sh.row_values(i, 1)
    tmp.sort()
    cities.append(tmp[int(len(tmp) / 2)])

positions = []
cs = (0, 0)
for i in range(1, 8):
    tmp = sh.col_values(i, 1)
    if sum(tmp) / len(tmp) > cs[1]:
        cs = (i, sum(tmp) / len(tmp))

print(max(cities))
print(cs)
