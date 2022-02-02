"""xls轉xlsx黨程式"""
for i in range(89,111):
    if i < 100 :
        i = "0"+str(i)
    else :
        i = str(i)

    fname = r"C:\Users\valtina\Desktop\read_excel\output_directory\m1s2-"+i+"00"
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)
    new_name = "C:\\Users\\valtina\\Desktop\\read_excel\\output_directory\\"+i
    wb.SaveAs(new_name, FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()
