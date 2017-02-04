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

def test_add_group():
    main_window = launch_application()
    old_groups_list = get_group_list(main_window)
    add_new_group(main_window, 'Test Group')
    new_groups_list = get_group_list(main_window)
    old_groups_list.append('Test Group')
    assert sorted(new_groups_list) == sorted(old_groups_list)
    close_application(main_window)


def launch_application():
    application = Application.Launch("C:\\Users\\Rostik\\Documents\\Code\\Addressbook\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    return main_window


def add_new_group(main_window, group_name):
    modal = open_groups_editor(main_window)
    modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
    modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(group_name)
    Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
    close_groups_editor(modal)


def open_groups_editor(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")
    return modal


def close_groups_editor(modal):
    modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()


def close_application(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()

def get_group_list(main_window):
    modal = open_groups_editor(main_window)
    tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
    groups_list = [node.Text for node in tree.Nodes[0].Nodes]
    close_groups_editor(modal)
    return groups_list