# web-scraping
This repo contains file for scraping the website https://www.consumeraffairs.com/sporting_goods/nike.html to extract the nike product reviews.
### Web Scraping : 
Web scraping is method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a database so that it can be used in various applications.
### Web Crawling: 
A web crawler or web spider, is a computer program that's used to search and automatically index website content and other information over the internet.To get to the next webpage, the crawler finds and follows hyperlinks that appear.

I have used python to define a crawler and scraper.
In main.py, BeautifulSoup package is used to define a web-crawling function and the dataset out.csv containing the reviews(html page content) is extracted using web scraping.
In datacleaning.ipynb, the data is cleanied using pandas and a csv file file.csv is created so that it can be used directly.
