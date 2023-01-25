
# 정규식 : Regular Expressions
#         정해진 형태를 의미하는 식 (주민번호, 이메일주소, 자동차번호판, IP주소 같은...)
#         그 조건 만족하는 것 찾아주는 것

import re
# 정규식 라이브러리 가져오기

# 네글자 중 세글자만 기억난다면... ca?e
# care, cafe, case, cafe.... 찾아야 하는데 어떻게??
# caae, cabe, cace.... 이렇게 하나씩 찾는것은 아니고...

# 1. p = re.compile("원하는 형태")      : 원하는 형태 쓰고
# 2. m = p.match("비교할 문자열")       : 처음부터 일치하는지?
# 3. m = p.search("비교할 문자열")      : 일치하는게 있는지?
# 4. lst = p.findall("비교할 문자열")   : 일치하는 것을 리스트로 반환

p = re.compile("ca.e")
# p   : 패턴을 의미
# 원하는 형태 = 정규식
# .   : 하나의 문자를 의미      > care, cafe, case 된다 | caffe 안된다
# ^   : 문자열의 시작 (^de)     > desk, destination 된다 | fade 안된다
# $   : 문자열의 끝 (se$)       > case, base 된다 | face 안된다


# 함수 정의하고 사용하기
def print_match(m):
    if m:
        print("m.group() :", m.group())     #일치하는 문자열을 반환
        print("m.string :", m.string)       #입력받은 문자열을 반환
        print("m.start() :", m.start())      #일치하는 문자열의 시작 index
        print("m.end() :", m.end())         #일치하는 문자열의 끝 index
        print("m.span() :", m.span())       #일치하는 문자열의 시작, 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("careless")     
# m = p.search("good care")
# print_match(m)
# match나 search중 하나 살려서 돌려보면 됨
# match     : 주어진 문자열의 처음부터 일치하는지 확인 (care, careless 모두 됨)
# search    : 주어진 문자열 중에 일치하는 것이 있는지 확인 (care, good care, careless 모두 됨)

lst = p.findall("good care cafe case")
print(lst)

# findall   : 주어진 문자열에서 일치하는 모든 것을 리스트 형태로 반환




