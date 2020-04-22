# downloads all the e-books
from bs4 import BeautifulSoup
import re
import requests
import time
import subprocess
import os

if not os.path.exists("ebooks"):
    os.mkdir("ebooks")
os.chdir("ebooks")

base_url = "https://link.springer.com"
with open("../books.txt", "r") as f1:
    for line in f1:
        page = requests.get(line)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find_all('title')[0].text.split("/")[0] # wget has issues renaming file with a `/`. We truncate the filename at this point if one exists.
        search_string = str(soup.find_all('div', class_='cta-button-container__item')[0])
        for i in range(0, len(search_string)):
            if search_string[i]=='h' and search_string[i+1] == 'r' and search_string[i+2] == 'e':
                tail_url = search_string[i+6:-1].split(" ")[0]
                full_url = base_url + tail_url
                print(f'Downloading {full_url}')
                output = subprocess.check_output(f'wget -cO \"{title}\" \"{full_url}', shell=True).decode()
        time.sleep(5)
