import FreeSimpleGUI.window
from functions import get_todos,write_todos
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo")

window = FreeSimpleGUI.Window('My To-Do App',layout=[[label,input_box]])
window.read()
window.close()