from comtypes.client import CreateObject
import os

# to save xlsx file inside of the project folder set project path as default
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_to_save = os.path.join(project_dir, "data/groups.xlsx")

# open Excel app
xl = CreateObject("Excel.Application")
# make it visible
xl.Visible = 1
wb = xl.Workbooks.Add()
# add data
for i in range(100):
    xl.Range["A%s" % (i + 1)].Value[()] = "group %s" % str(i+1)
wb.SaveAs(file_to_save)
xl.Quit()
