from openpyxl.descriptors.base import String
import requests
from bs4 import BeautifulSoup

url = "https://comp.fnguide.com"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("div", attrs={"id":"highlight_D_Y"}).find("table", attrs={"class":"us_table_ty1 h_fix zigbg_no"}).find("tbody").find_all("tr")

for row in data_rows:
    columns = row.find("td")
    data = [column.get_text() for column in columns]
    print(data)
    print("-------")
    print(map(float, data))