import shutil
import pathlib
import os


def copy_common_steps():
    original = f'{pathlib.Path(__file__).parent.resolve()}/files_for_user/common_steps_copy.py'
    target = f'{os.getcwd()}/steps/common_steps_pb_testing.py'

    shutil.copyfile(original, target)
    print("Copied common_steps from library!")


def create_new_action_file():
    with open(f'{os.getcwd()}/steps/new_actions.py', "w") as f:
        f.write('from behave import *\n')
    with open(f'{os.getcwd()}/steps/new_steps.py', "w") as f:
        f.write('from behave import *\n')
    print("Created files for generating actions and plans :D!")


def copy_behave_environment_file():
    original = f'{pathlib.Path(__file__).parent.resolve()}/files_for_user/environment_copy.py'
    target = f'{os.getcwd()}/environment.py'

    shutil.copyfile(original, target)
    print("Created environment file!")
