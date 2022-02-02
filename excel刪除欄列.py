wb = load_workbook(filename)
ws = wb.active
for i in range(1,4):
    ws.delete_rows(1)
for i in range(1,11):
    ws.delete_rows(2)
ws.delete_cols(3)
ws.delete_cols(3)
for i in range(1,24):
    p=i*6+3-i
    ws.delete_cols(p)

wb.save(filename)
