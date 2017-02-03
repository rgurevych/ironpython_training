import clr
import sys
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "TestStack.White.9.2.0.11\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.1.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application

def test_something():
    Application.Launch("notepad.exe")
    print("Hello, World!")

