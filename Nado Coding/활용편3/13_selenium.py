#210908 시작만  동영상의 2:56:22~
# 크롬에서 주소창에 "chrome://version/"쳐서 버전 확인
# 구글에서 ChromeDriver 검색해서 크롬드라이버 다운받기


from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
#   크롬 드라이버가 같은 폴더 안에 있으면 빈 괄호만 해줘도 된다. (또는 "./chromedriver.exe")
#   그렇지 않다면 크롬 드라이버의 경로를 괄호 안에 넣어줘야 한다.

browser.get("http://naver.com")