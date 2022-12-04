import sqlite3


def setup():
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
                                (url VARCHAR)''')
        conn.commit()
    else:
        print('Table for user data exists')

    conn.close()


def save_urls(urls):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    c.execute("""DELETE FROM urls_and_attributes""")
    c.execute("""DELETE FROM original_urls""")

    conn.commit()
    for url in urls:
        c.execute("""insert into urls_and_attributes(url) values(?)""", [url])
        c.execute("""insert into original_urls(url) values(?)""", [url])
    conn.commit()
    conn.close()


def retrieve_urls(database_name):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    #line below will return array of strings, instead of array of tuples
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    urls = c.execute(f"SELECT url from {database_name}").fetchall()
    conn.close()
    return urls


def add_url(url):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    c.execute(f"INSERT INTO urls_and_attributes(url) values('{url}')")
    conn.commit()
    conn.close()


def delete_url(url):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')

    c = conn.cursor()
    c.execute(f"DELETE FROM urls_and_attributes where url='{url}'")
    conn.commit()
    conn.close()


def rename_url(url, new_url):
    conn = sqlite3.connect('resources_for_testing/handy.sqlite')
    c = conn.cursor()
    c.execute(f'UPDATE urls_and_attributes set url=\'{new_url}\' where url=\'{url}\'')
    conn.commit()
    conn.close()
