import xlrd

excel = 'F:/sele_po_demo/data/testData.xlsx'
data = xlrd.open_workbook(excel)
table  = data.sheet_by_name('username')
nrow  = table.nrows

for i in range(1,nrow):
    print(table.cell(i, 1))