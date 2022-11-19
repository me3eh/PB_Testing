from services import actions_to_steps_transform
import PySimpleGUI as sg
from shared_info.constants import OK_PNG

def generate_plan(window, todo_actions):
    test_title = window['-TITLE-OF-TEST-'].get()
    actions_to_steps_transform.create(todo_actions, test_title, 'given')
    sg.popup_notify("Created", icon=OK_PNG)
