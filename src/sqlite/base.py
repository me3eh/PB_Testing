import sqlite3


def database_setup():
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    table_exists = c.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='urls_and_attributes'; """).fetchall()

    if not table_exists:
        print('Creating database')
        c.execute('''CREATE TABLE urls_and_attributes
                        (url VARCHAR,
                        ids TEXT,
                        input_names TEXT,
                        css_classes TEXT)''')
        conn.commit()

    print('Database was already created')
    conn.close()


def database_save_urls(objects):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    for object in objects:
        c.execute("""insert into urls_and_attributes(url) values(?)""", [object])
    conn.commit()
    conn.close()


def database_retrieve_urls():
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    urls = c.execute("""SELECT url from urls_and_attributes""").fetchall()
    conn.close()
    return urls

# database_save_urls(['da', 'no', 'ca'])