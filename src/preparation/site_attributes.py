
from scenario_helper.file_helper import read_from_file, write_to_file_array, create_dir
from site_scraping.site_info import get_browser_attributes
# from configparser import ConfigParser


def scrap_attributes_from_site(url):
    # urls = read_from_file("resources_for_testing/url.txt")
    # config = ConfigParser()
    # config.read('resources_for_testing/config.ini')
    # domain = config.get('main', 'domain')

    for index, url in enumerate(urls):
        attributes = get_browser_attributes(domain + url)

        for attribute in attributes.keys():
            url_for_path = url.replace('/', 'root/', 1)

            # dir_name_with_path = f"resources_for_testing/{url_for_path}"
            # create_dir(dir_name_with_path)
            # write_to_file_array(file_name=f"{dir_name_with_path}/{attribute}", file_inside=attributes[attribute])
