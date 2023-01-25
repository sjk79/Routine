import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 가져온 html 문서를 lxml 파서를 이용해서 뷰티플숩 객체로 만들어라

#print(soup.title)                  # Soup              : 객체 아래있는 title이라는 엘리먼트에 접근하는 것
#print(soup.title.get_text())       # get_text()        : 글자만 빼오기


#print(soup.a)                      #: soup.a           : 숩의 모든 객체 중 첫번째 발견되는 a 엘리먼트 출력
#print(soup.a.attrs)                #: soup.a.attrs     : a 엘리먼트의 속성 정보 출력
#print(soup.a["href"])              #: soup.a["속성"]   : a 엘리먼트의 속성값 정보를 출력


#print(soup.find("a", attrs={"class":"Nbtn_upload"}))    #숩 객체 중 A테그에서 클래스 속성이 엔버튼업로드인것
#print(soup.find(attrs={"class":"Nbtn_upload"}))         #테그명시 안해되 된다
#print(soup.find(attrs={"class":"Nbtn_upload"}).get_text())


#print(soup.find("li", attrs={"class":"rank01"}))        #li 테그의 클래스명 rank01 찾기

rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a)
#print(rank1.a.get_text())

#rank2 = rank1.next_sibling.next_sibling
#print(rank2.a.get_text())

#rank3 = rank2.next_sibling.next_sibling
#print(rank3.a.get_text())

#rank2 = rank3.previous_sibling.previous_sibling
#print(rank2.a.get_text())

#print(rank1.parent)

#rank2 = rank1.find_next_sibling("li")                   # li에 해당하는 테그의 next sibling 찾기
#print(rank2.a.get_text())

#rank3 = rank2.find_next_sibling("li")
#print(rank3.a.get_text())

#rank2 = rank3.find_previous_sibling("li")
#print(rank2.a.get_text())

#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="엽총소년-28화")
print(webtoon)
