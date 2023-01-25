import requests

res = requests.get("http://naver.com")
res.raise_for_status()

# 처음에 항상 이렇게 쓰는것을 습관적으로 하면 됨
# raise_for_status()   : 문제가 생겼을때 오류를 출력하고 프로그램 끝내는 것
# res.status_code      : 200이 나오면 정상적으로 페이지 접근하는 것, 403이면 접근권한 없는 것

print(len(res.text))
# res     : 가져온
# .text   : html 문서의
# len()   : 길이를
# print() : 보여줘

print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

# 파일로 만들기
# w : 쓰기모드