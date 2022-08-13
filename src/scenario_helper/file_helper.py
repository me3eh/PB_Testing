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
