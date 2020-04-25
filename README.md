# Springer textbooks webscraper

This is a webscraper to download the FREE Springer textbooks from the [Springer website](https://docs.google.com/spreadsheets/d/1JG1J1pynfh0NLWVsDX8Y9MhJoHSVoQX95IrU9uv4Qnw/edit#gid=1612330180). These textbooks are available until July.

This program differs from other projects. Namely, that it does not download the `.epub` extensions -- only the PDF. It also is a webscraper, unlike the leading popular Python port of this type of program which downloads the scripts based on their url.

# To Run the program

1) Currently the books inside here are all the `.pdf` books in the Excel spreadsheet. If you would like to only download certain books, 
add links from the `OpenURL` tab in the Excel spreadsheet into the `books.txt` file.

2) run `pip install -r requirements.txt` to install BeautifulSoup and the wget dependency.

3) run `python3 download.py` to begin the download and see the output.

4) open the `ebooks` folder that is created and your downloads should be present.

# System Requirements
Windows, macOS, or Linux

# Known Bugs
On each download, this program renames the filename to the title of the respective textbook.
This is fine, but when a `/` exists there is an error. This scraper modifies the title to a `/` to remove the error.

# Improvements
1) continuing to the next link after failure:

# Thanks

Thanks to Teal Dulcet for coming up with a better `/` solution than mine, as well as alerting me to an issue regarding duplicate book titles + authors
which caused some books to be overwritten.
