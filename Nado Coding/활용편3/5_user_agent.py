import requests

url="https://nadocoding.tistory.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}
# headers 값 찾기 위해서 구글에서 user agent string 검색
# What is my User Agent? 싸이트 들어가서 나의 값 받아오기

res = requests.get(url, headers=headers)

#res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)


