import clr
import sys
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")
clr.AddReferenceByName("UIAutomationTypes, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *
from System.Windows.Automation import *
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    app_path = request.config.getoption("--path")
    fixture = launch_application(app_path)
    request.addfinalizer(close_application)
    return fixture

def launch_application(app_path):
    application = Application.Launch(app_path)
    main_window = application.GetWindow("Free Address Book")
    return main_window

def close_application():
    global fixture
    fixture.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()


def pytest_addoption(parser):
    parser.addoption("--path", action="store", default="C:\\Users\\Rostik\\Documents\\Code\\Addressbook\\AddressBook.exe")