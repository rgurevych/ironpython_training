import clr
import sys
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
clr.AddReferenceByName("TestStack.White")
clr.AddReferenceByName("UIAutomationTypes, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")

from TestStack.White import Application
from TestStack.White.UIItems.Finders import *
from System.Windows.Automation import *
from Microsoft.Office.Interop import Excel
import pytest
from models.group import Group

fixture = None
test_data = ["group1", "group2", "group3"]

@pytest.fixture(scope = "session")
def app(request):
    global fixture
    app_path = request.config.getoption("--path")
    fixture = launch_application(app_path)
    request.addfinalizer(close_application)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            #test_data = ["group1", "group2", "group3"]
            test_data = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[x for x in test_data])


def launch_application(app_path):
    application = Application.Launch(app_path)
    main_window = application.GetWindow("Free Address Book")
    return main_window

def close_application():
    global fixture
    fixture.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()


def load_from_xlsx(file):
    excel = Excel.ApplicationClass()
    excel.Visible = True
    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % file)
    workbook = excel.Workbooks.Open(data_file)
    sheet = workbook.ActiveSheet
    i = 1
    test_data = []
    while sheet.Range["A%s" % i].Value2:
        test_data.append(Group(name=sheet.Range["A%s" % i].Value2))
        i = i+1
    excel.Quit()
    return test_data


def pytest_addoption(parser):
    parser.addoption("--path", action="store", default="C:\\Users\\Rostik\\Documents\\Code\\Addressbook\\AddressBook.exe")