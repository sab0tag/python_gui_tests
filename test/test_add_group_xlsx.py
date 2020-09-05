import pytest
from comtypes.client import CreateObject
import os


# to save xlsx file inside of the project folder set project path as default
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_to_save = os.path.join(project_dir, "data/groups.xlsx")

# open Excel app
xl = CreateObject("Excel.Application")
# make it visible
xl.Visible = 1
wb = xl.Workbooks.Open(file_to_save)
ws = wb.Worksheets(1)
data_list = []
for each_row in range(1, 99):
    dynamic_data = ws.Cells[each_row, 1].Value[()]
    data_list.append(dynamic_data)
xl.Quit()


@pytest.mark.parametrize("group", data_list, ids=[repr(x) for x in data_list])
def test_load_groups(group):
    pass
