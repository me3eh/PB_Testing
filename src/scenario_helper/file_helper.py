# universal way of reading from and writing to files. Need full file path :D
import os


def read_from_file(file_name):
    file_inside = []
    try:
        with open(file_name, "r") as file:
            for readline in file:
                line_strip = readline.strip()
                file_inside.append(line_strip)
        return file_inside
    except:
        return None


def write_to_file(file_name, file_inside):
    with open(file_name, 'w') as f:
        f.write(file_inside)


def write_to_file_array(file_name, file_inside):
    with open(file_name, 'w') as f:
        for index, element in enumerate(file_inside):
            if index != 0:
                f.write("\n")
            f.write(element)


def create_dir(dir_name_with_path):
    is_exist = os.path.exists(dir_name_with_path)
    print(f'Creating {dir_name_with_path}')
    if not is_exist:
        os.makedirs(dir_name_with_path)
