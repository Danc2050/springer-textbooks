# Springer textbooks webscraper

This is a webscraper to download the FREE Springer textbooks from the [Springer website](https://docs.google.com/spreadsheets/d/1JG1J1pynfh0NLWVsDX8Y9MhJoHSVoQX95IrU9uv4Qnw/edit#gid=1612330180). These textbooks are available until July.

**WARNING** This has only been tested on the Computer Science section of textbooks. Not all links may be setup the same on the Springer website, and in such a case this program will fail. There is also an issue with titles that have a `/` in them (see *Known Bugs* section below)

# To Run the program

1) Enter the `OpenURL` links from the Excel spreadsheet in the `books.txt`. (Currently the books inside here are all the Computer Science books in the Excel spreadsheet).

2) run `pip install -r requirements.txt` to install BeautifulSoup dependency.

3) run `python3 download.py` to begin the download and see the output.

# System Requirements
One must be running a system that has `wget` installed.

# Known Bugs
On each download, this program renames the filename to the title of the respective textbook.
This is fine, but when a `/` exists there is an error. This scraper truncates the name of the textbook before the `/` to complete the download.

# Improvements
There are many improvements that can be done such as:

1) continuing to the next link after failure:

2) not shutting the program done if it fails

3) verifying that this program works on all links published by Springer
