from bs4 import BeautifulSoup
import re
import requests
import time
import subprocess
import os
import wget

if not os.path.exists("ebooks"):
    os.mkdir("ebooks")
os.chdir("ebooks")

base_url = "https://link.springer.com"
with open("../books.txt", "r") as f1:
    for line in f1:
        page = requests.get(line)
        soup = BeautifulSoup(page.content, 'html.parser')

        # wget has issues renaming file with a `/`. We replace it with a ' ' if a '/' exists.
        title = soup.title.text.split("| SpringerLink")[0].replace("/", " ").rstrip()
        #authors = soup.find(class_="authors__name").text # optionally, add this to var output
        isbn = soup.find(id="print-isbn").text
        output = f'{title} {isbn}.pdf'
        search_string = str(soup.find_all('div', class_='cta-button-container__item')[0])
        for i in range(0, len(search_string)):
            if search_string[i]=='h' and search_string[i+1] == 'r' and search_string[i+2] == 'e': # probably a better way to do this
                tail_url = search_string[i+6:-1].split(" ")[0]
                full_url = base_url + tail_url
                print(f'Downloading {full_url}')
                wget.download(full_url, out=output)
