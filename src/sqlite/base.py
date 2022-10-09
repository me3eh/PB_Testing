import sqlite3


def database_setup():
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    table_with_original_urls_exists = c.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='original_urls'; """).fetchall()

    table_with_user_data_exists = c.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='urls_and_attributes'; """).fetchall()

    if not table_with_original_urls_exists:
        print('Creating table for project urls in database')
        c.execute('''CREATE TABLE original_urls
                        (url VARCHAR)''')
        conn.commit()
    else:
        print('Table for project urls exists')

    if not table_with_user_data_exists:
        print('Creating table for user data in database')
        c.execute('''CREATE TABLE urls_and_attributes
                                (url VARCHAR,
                                ids TEXT,
                                input_names TEXT,
                                css_classes TEXT)''')
        conn.commit()
    else:
        print('Table for user data exists')

    conn.close()


def database_save_urls(objects):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    for object in objects:
        c.execute("""insert into urls_and_attributes(url) values(?)""", [object])
        c.execute("""insert into original_urls(url) values(?)""", [object])
    conn.commit()
    conn.close()


def database_retrieve_urls(database_name):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    urls = c.execute(f"SELECT url from {database_name}").fetchall()
    conn.close()
    return urls


def database_retrieve_attribute(attribute, url):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    urls = c.execute(f"SELECT {attribute} from urls_and_attributes where url='{url}'").fetchall()
    conn.close()
    return urls

# c = database_retrieve_urls('urls_and_attributes')
# print(c)