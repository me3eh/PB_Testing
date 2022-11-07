import shutil
import pathlib
import os


def copy_common_steps():
    original = f'{pathlib.Path(__file__).parent.resolve()}/common_steps_copy.py'
    target = f'{os.getcwd()}/steps/common_steps.py'

    shutil.copyfile(original, target)
    print("Copied common_steps from library!")
