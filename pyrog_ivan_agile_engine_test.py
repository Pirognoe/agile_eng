import requests
import sys
from bs4 import BeautifulSoup

# Lets declare variables to contain urls to our web-sites:
input_origin_file_path = sys.argv[1]
input_other_sample_file_path = sys.argv[2]

# Lets declare variables to contain request results (GET method):
origin_page = requests.get(input_origin_file_path)
other_page = requests.get(input_other_sample_file_path)

# Lets make the Soup:
origin_page_soup = BeautifulSoup(origin_page.text, features="lxml")
other_page_soup = BeautifulSoup(other_page.text, features="lxml")

button_origin_search_result_list = origin_page_soup.find_all('a', attrs={"class": "btn btn-success", "onclick": True})
button_other_search_result_list = other_page_soup.find_all('a', attrs={"class": "btn btn-success", "onclick": True})


def xpath_builder(search_results_tags):
    """Function to assemble Xpath of the given list of Beautiful Soup tags found
    :type search_results_tags: list
    """
    output = ""
    for item in search_results_tags:
        xml_elements_list = []
        for parent in item.parents:
            xml_elements_list.append(parent.name)
        xml_elements_list.reverse()
        output = "/".join(xml_elements_list[1:]) + "/" + item.name
    return output


print(f"The original page Xpath: {xpath_builder(button_origin_search_result_list)}")
print(f"The updated page Xpath: {xpath_builder(button_other_search_result_list)}")
