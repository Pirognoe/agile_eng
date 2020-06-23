import requests
import sys
from bs4 import BeautifulSoup

# Lets declare variables to contain urls to our web-sites:
"""input_origin_file_path = sys.argv[1]"""
"""input_other_sample_file_path = sys.argv[2]"""
input_origin_file_path = "https://agileengine.bitbucket.io/beKIvpUlPMtzhfAy/samples/sample-0-origin.html"
input_other_sample_file_path_1 = "https://agileengine.bitbucket.io/beKIvpUlPMtzhfAy/samples/sample-1-evil-gemini.html"
input_other_sample_file_path_2 = "https://agileengine.bitbucket.io/beKIvpUlPMtzhfAy/samples/sample-2-container-and-clone.html"
input_other_sample_file_path_3 = "https://agileengine.bitbucket.io/beKIvpUlPMtzhfAy/samples/sample-3-the-escape.html"
input_other_sample_file_path_4 = "https://agileengine.bitbucket.io/beKIvpUlPMtzhfAy/samples/sample-4-the-mash.html"


# Lets declare variables to contain request results (GET method):
origin_page = requests.get(input_origin_file_path)
other_page_1 = requests.get(input_other_sample_file_path_1)
other_page_2 = requests.get(input_other_sample_file_path_2)
other_page_3 = requests.get(input_other_sample_file_path_3)
other_page_4 = requests.get(input_other_sample_file_path_4)


# Lets make the Soup:
origin_page_soup = BeautifulSoup(origin_page.text,  features="lxml")
other_page_soup_1 = BeautifulSoup(other_page_1.text, features="lxml")
other_page_soup_2 = BeautifulSoup(other_page_2.text, features="lxml")
other_page_soup_3 = BeautifulSoup(other_page_3.text, features="lxml")
other_page_soup_4 = BeautifulSoup(other_page_4.text, features="lxml")


print(origin_page_soup.find_all('a', attrs={"class": "btn btn-success"}))
print(other_page_soup_1.find_all('a', attrs={"class": "btn btn-success"}))
print(other_page_soup_2.find_all('a', attrs={"class": "btn btn-success"}))
print(other_page_soup_3.find_all('a', attrs={"class": "btn btn-success"}))
print(other_page_soup_4.find_all('a', attrs={"class": "btn btn-success"}))