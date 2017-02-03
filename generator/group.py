import string
import random
import re
import os.path
import getopt
import sys
import clr
from models.group import Group
import time

clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "C:\Users\Rostik\Documents\Code\ironpython_training\data\groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(max_length):
    sym = string.ascii_letters + string.digits + " "*10
    #The following string generates random string, replaces duplicated spaces with only one and deletes space in the end
    return re.sub('\s+', ' ', ("".join([random.choice(sym)
                                                 for i in range(random.randrange(max_length))]).rstrip()))

testdata = [Group(name="")] + [Group(name=random_string(15)) for i in range(n)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

excel = Excel.ApplicationClass()
excel.Visible = True

workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet

for i in range(len(testdata)):
    sheet.Range["A%s" % (i+1)].Value2 = testdata[i].name

workbook.SaveAs(f)

time.sleep(10)

excel.Quit()