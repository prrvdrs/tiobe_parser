from bs4 import BeautifulSoup
import requests
import csv

# Parse the html content

page = requests.get("https://www.tiobe.com/tiobe-index/")
soup = BeautifulSoup(page.content, "html.parser")

# Preparing the CSV file
csvfile = open('index_tiobe.csv', 'w')
writer = csv.writer(csvfile, delimiter=',',lineterminator='\n',quotechar = '"')
writer.writerow(["Period","Rank","Language","Rating"])

tables = soup.find_all("table")
mytable = tables[0]


# Find all rows (tag <tr>):
trs = mytable.find_all("tr")

for rows in trs[1:]:
    cols = rows.find_all(['th', 'td'])
    month_year = "2019-01-01"
    rank = cols[0].text
    language = cols[3].text
    rating = cols[4].text
    change = cols[5].text
    writer.writerow( [month_year, rank, language, rating]  )