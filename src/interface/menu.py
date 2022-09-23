import os
from scenario_helper.scenario import Scenario
from scenario_helper.feature import Feature
from simple_term_menu import TerminalMenu
from scenario_helper.file_helper import write_to_file
from scenario_helper.actions import Actions
import time

MAIN_MENU_OPTIONS = ["Edit filename", "Edit feature", "Edit scenario", "Save file", "Quit"]
EDIT_SCENARIO_ARRAY_OPTIONS = ["Add scenario", "Edit scenario", "Delete scenario", "Return to Main Menu"]
EDIT_SCENARIO_OPTIONS = ["Change scenario",
                         "Add Given", "Change given", "Remove given",
                         "Add When", "Change when", "Remove when",
                         "Add then", "Change then", "Remove then",
                         "Return to Main Menu"]
EDIT_GIVEN_OPTIONS = [Actions('visiting url ', 'url'), Actions('logged as admin'), Actions('logged as user'),
                        Actions('logged as user'), Actions('click on button with id ', 'id'), 'Abort']
EDIT_WHEN_OPTIONS = [Actions('visiting url ', 'url'), Actions('logged as admin'), Actions('logged as user'),
                        Actions('logged as user'), Actions('click on button with id ', 'id'), 'Abort']
EDIT_THEN_OPTIONS = [Actions('site title should have name ', 'name'), Actions('site url should be ', 'url')]
scenarios = [Scenario()]
feature = Feature()
breadcrumbs = []

main_menu_exit = False
edit_scenario_exit = False
choose_scenario_exit = False
edit_scenario_array_exit = False
scenario_exit = False
given_exit = False
when_exit = False
then_exit = False

def join_array(array, word_between):
    return word_between.join(str(x) for x in array)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def monit_with_information(text):
    cls()
    print(text)
    time.sleep(2)


def print_out_whole_feature_description():
    print(feature.get_as_string())
    for scenario in scenarios:
        print(scenario.get_as_string())
        print(join_array(breadcrumbs, "->"))


def terminal_menu(options):
    return TerminalMenu(options).show()


def main_menu():
    breadcrumbs.append('MainMenu')
    global main_menu_exit
    while not main_menu_exit:
        cls()
        print_out_whole_feature_description()
        choice = terminal_menu(options=MAIN_MENU_OPTIONS)
        if choice == 0:
            file_name = input("Give me your file_name")
            feature.set_filename(file_name)
        if choice == 1:
            feature_text = input("Give me your feature name")
            feature.set_feature_description(feature_text)
        if choice == 2:
            edit_scenario_array_menu()
        if choice == 3:
            feature_description = feature.get_as_string_only_feature_description()
            scenario_description = ''
            for scenario in scenarios:
                scenario_description += scenario.get_as_string()
            file_name = feature.get_filename()
            final_text_for_file = feature_description + "\n" + scenario_description
            write_to_file(file_name=file_name, file_inside=final_text_for_file)
            monit_with_information(f"Succesfully saved \nLook for it under /features/{file_name}")

        if choice == is_it_last(option=MAIN_MENU_OPTIONS):
            main_menu_exit = True

    cls()
    print("Bye bye")
    return 0

def edit_scenario_array_menu():
    breadcrumbs.append('ScenarioManagement')
    global edit_scenario_array_exit
    while not edit_scenario_array_exit:
        cls()
        print_out_whole_feature_description()
        choice = terminal_menu(options=EDIT_SCENARIO_ARRAY_OPTIONS)
        if choice == 0:
            scenarios.append(Scenario())
        if choice == 1:
            choose_scenario_menu()
        if choice == 2:
            scenarios.pop()

        if choice == is_it_last(option=EDIT_SCENARIO_ARRAY_OPTIONS):
            edit_scenario_array_exit = True
            breadcrumbs.pop()
    edit_scenario_array_exit = False


def choose_scenario_menu():
    breadcrumbs.append("ChooseScenario")
    global choose_scenario_exit
    while not choose_scenario_exit:
        cls()
        print_out_whole_feature_description()
        menu_scenarios = list(map(Scenario.get_scenario_name, scenarios)) + ["Return to Previous Menu"]
        choice = terminal_menu(options=menu_scenarios)
        if choice == is_it_last(option=menu_scenarios):
            choose_scenario_exit = True
            breadcrumbs.pop()
            break

        scenario_menu(choice)

    choose_scenario_exit = False


def scenario_menu(index):
    breadcrumbs.append("EditScenario")
    global scenario_exit
    while not scenario_exit:
        cls()
        print_out_whole_feature_description()
        choice = terminal_menu(options=EDIT_SCENARIO_OPTIONS)
        if choice == 0:
            scenarios[index].set_scenario_name( input("Change scenario name") )
        if choice == 1:
            scenarios[index].add_given()
        if choice == 2:
            pick_type_given_to_change_text(index)
        if choice == 3:
            scenarios[index].remove_given()
        if choice == 4:
            scenarios[index].add_when()
        if choice == 5:
            pick_type_given_to_change_text(index)
        if choice == 6:
            scenarios[index].remove_when()
        if choice == 7:
            scenarios[index].add_then()
        if choice == 8:
            pick_type_given_to_change_text(index)
        if choice == 9:
            scenarios[index].remove_then()

        if choice == is_it_last(option=EDIT_SCENARIO_OPTIONS):
            scenario_exit = True
            breadcrumbs.pop()
    scenario_exit = False

def pick_type_given_to_change_text(index):
    breadcrumbs.append("Edit_GIVEN")
    global given_exit
    while not given_exit:
        cls()
        print_out_whole_feature_description()
        full_menu_for_givens = scenarios[index].givens + ["Return to previous menu"]
        choice = terminal_menu(options=full_menu_for_givens)
        if choice == is_it_last(option=full_menu_for_givens):
            given_exit = True
            breadcrumbs.pop()
            break
        breadcrumbs.append("List of givens")
        list_of_givens_options = map(to_string, EDIT_GIVEN_OPTIONS)
        side_choice = terminal_menu(options=list_of_givens_options)
        if side_choice != is_it_last(option=EDIT_GIVEN_OPTIONS):
            text = EDIT_GIVEN_OPTIONS[side_choice].output()
            scenarios[index].set_given(text, choice)
        breadcrumbs.pop()

    given_exit = False


def pick_type_when_to_change_text(index):
    breadcrumbs.append("Edit_WHEN")
    global when_exit
    while not when_exit:
        cls()
        print_out_whole_feature_description()
        full_menu_for_whens = scenarios[index].whens + ["Return to previous menu"]
        choice = terminal_menu(options=full_menu_for_whens)
        if choice == is_it_last(option=full_menu_for_whens):
            when_exit = True
            breadcrumbs.pop()
            break
        breadcrumbs.append("List of givens")
        list_of_whens_options = map(to_string, EDIT_WHEN_OPTIONS)
        side_choice = terminal_menu(options=list_of_whens_options)
        if side_choice != is_it_last(option=EDIT_WHEN_OPTIONS):
            text = EDIT_WHEN_OPTIONS[side_choice].output()
            scenarios[index].set_when(text, index)
        breadcrumbs.pop()

    when_exit = False

def pick_type_then_to_change_text(index):
    breadcrumbs.append("Edit_WHEN")
    global then_exit
    while not then_exit:
        cls()
        print_out_whole_feature_description()
        full_menu_for_thens = scenarios[index].thens + ["Return to previous menu"]
        choice = terminal_menu(options=full_menu_for_thens)
        if choice == is_it_last(option=full_menu_for_thens):
            then_exit = True
            breadcrumbs.pop()
            break
        breadcrumbs.append("List of givens")
        list_of_thens_options = map(to_string, EDIT_THEN_OPTIONS)
        side_choice = terminal_menu(options=list_of_thens_options)
        if side_choice != is_it_last(option=EDIT_THEN_OPTIONS):
            text = EDIT_THEN_OPTIONS[side_choice].output()
            scenarios[index].set_then(text, index)
        breadcrumbs.pop()

    when_exit = False


def is_it_last(option):
    return len(option) - 1


def to_string(name):
    return str(name)
