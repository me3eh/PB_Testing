import os
from preparation.create_directory import create_dir
import pytest

def delete_dirs(dirs):
    for directory in dirs:
        is_exist = os.path.exists(directory)
        if is_exist:
            os.removedirs(directory)

@pytest.fixture(autouse=True)
def run_around_tests():
    delete_dirs(["cc"])
    yield
    delete_dirs(["cc"])

def test_create_dir():
    assert os.path.exists('cc') is False
    create_dir(['cc'])
    assert os.path.exists('cc') is True

