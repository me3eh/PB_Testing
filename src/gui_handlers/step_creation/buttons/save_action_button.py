# from services.add_action import action_create
# from shared_info.constants import ERROR_PNG
# import PySimpleGUI as sg
#
# def save_action(window, values, current_tags, todo_actions):
#     bdd_attribute = window['-BDD-ATTRIBUTE-'].get()
#     type_of_action = values['-ACTIONS-CHOICE-']
#     input_for_action = values['-HELPER-INPUT-']
#     selected_action_index = window['-ACTION-LIST-'].get_indexes()
#     selected_tag = window['-TAG-LIST-'].get_indexes()
#     xpath_of_element = window['-XPATH-INPUT-'].get()
#
#     if len(selected_action_index) == 0:
#         sg.popup_notify("You didnt chose anything from todo_actions listbox to change", icon=ERROR_PNG)
#         return
#
#     new_action = action_create(type_of_action, selected_action_index, input_for_action,
#                                bdd_attribute, window, selected_tag, current_tags, xpath=xpath_of_element)
#     if not new_action:
#         sg.popup_notify("You didnt chose anything fromtodo actions listbox to change",
#                         icon=ERROR_PNG)
#         return
#
#     todo_actions[selected_action_index[0]] = new_action
#     window['-ACTION-LIST-'].update(create_todo_actions_for_listbox(todo_actions))
#
#
# def create_todo_actions_for_listbox(todo_actions):
#     return list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))
