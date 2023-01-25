#   210908 동영상의 2:41:11~
#   CSV1 네이버 금융
#   웹 스크레이핑으로 가져온 데이터를 CSV 파일로 저장

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# split("\t") 탭으로 구분한 데이터가 리스트 타입으로로 들어감
print(type(title))
writer.writerow(title)

for page in  range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

#   페이지 중 확인하려는 부분의 구성이
#   <table                  표
#       <thead>...          각 열의 의미
#       <tbody>             각 열의 의미
#           <tr>            행
#               <th>        열 제목
#               <td>        내용이 들어가는 쎌
#       <tfoot>             각 열의 의미

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    #   테이블 가져와서  --> 그중에 <tbody>  --> 그 아래서 tr을 find_all로하면 --> 데이터는 리스트 형태로 저장됨
    for row in data_rows:
        columns = row.find_all("td")
        # tr (한줄)에서 td 가져옴
        if len(columns) <= 1: # 의미없는 한줄 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # 한줄 for 문...
        # strip 함수 : 불필요한거 제거??

        writer.writerow(data)  #writerow() 안에는 리스트형으로 들어가야 함