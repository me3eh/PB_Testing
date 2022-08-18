import os


def create_dir(paths):
    # Check whether the specified path exists or not
    for path in paths:
        is_exist = os.path.exists(path)
        if not is_exist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            print(f"The directory {path} was created!")
        else:
            print(f"The directory {path} already exists!")
