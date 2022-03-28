from bs4 import BeautifulSoup
import requests

link = "https://www.karnataka.com/govt/district-wise-covid-19-cases/"

page = requests.get(link)
soup = BeautifulSoup(page.text,'html.parser')

table = soup.find("table",{"class":"info-table"})
rows = table.find_all("tr")
rows = rows[1:]

grandResult = []
for row in rows:
    result = []
    tableDataColumns = row.find_all("td")
    for tableDataColumn in tableDataColumns:
        result.append(tableDataColumn.getText())
    grandResult.append(result)

print(grandResult)
print(grandResult[0])
print(f'City Name':{grandResult[0]})
