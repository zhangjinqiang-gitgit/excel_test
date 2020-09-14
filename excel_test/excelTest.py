

import xlrd

wd = xlrd.open_workbook("./data.xlsx")
sheet = wd.sheets()[0]
for a in range(sheet.nrows):
    print()
    for b in range(sheet.ncols):
        cols = sheet.col_values(b)
        print(cols[b])