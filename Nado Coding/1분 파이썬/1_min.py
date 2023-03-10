# '22.07.20 21:00시작
#------------------------------------------------------------------------------
# (1) 소개
#------------------------------------------------------------------------------
# (2) 환경설정
#       --> 파이썬 설치
#       --> Visual Studio Code 설치
#       --> Visual Studio Code에서 Python extention 설치
#       --> Hello World 출력
print('hello world')
#------------------------------------------------------------------------------
# (3) 자료형
#     문자자료형      :정수, 실수 숫자 그대로 쓰기
print(1)
print(3.14)
#     숫자자료형      : '  ' 또는 "  "로 감싸기, 숫자도 감싸면 문자가 됨
print('hello wolrd')
print("안녕하세요")
print('10')
#     불리안자료형    : True, False, 시작문자 T와 F는 반드시 대문자로
print(True)
print(False)
#------------------------------------------------------------------------------
# (4) 변수
#       --> 세배돈을 봉투에 넣어 전달힌다.... 그러면 봉투는 변수, 세배돈은 값
#       --> 변수 선언   : 변수이름 = 값
envelope1 = 10000
envelope2 = 20000
envelope3 = '파이팅'
print(envelope1)
print(envelope2)
print(envelope3)
#------------------------------------------------------------------------------
# (5) 변수이름
#       ---> 변수이름의 규칙
#               문자 또는 언더바(_)로 시작한다, 숫자로 시작할 수 없다
#               문자, 숫자, 언더바로 구성된다
#               공백이나 특수문자 사용불가
#               대소문자 구분됨
#               키워드(예약어)는 사용할 수 없음
#                   약 30개의 키워드 있음-- ex) True, False, for, while, if continue, break, class 등
#               가독성위해 소문자로된 단어 또는 밑줄로 구분된 단어조합으로 하는게 좋음
name = '1분'
_name = '파이썬'
name123 = '빠르게'
name_456 = '배워요'
Name = "1분 - 첫글자 대문자 변수"
NAME = "1분 - 모든글자 대문자 변수"

print(name)
print(_name)
print(name123)
print(name_456)
print(Name)
print(NAME)
#------------------------------------------------------------------------------
# (6) 형변환
#       숫자와 문자는 더할 수 없음 -- ex)  2 + '2'
#       정수로 변환하기 : int()   --> 반올림 아닌 버림으로 정수가 된다
#       실수로 변환하기 : float()
#       문자로 변환하기 : str()
#       불리안으로 변환 : bool()

num = int('2')
print(num*2)
# int('two') 요런거 변환 안됨
# int('2.5') 요것도 바로 변환 안됨, int(float('2.5')) 요렇게 해야 변환 됨

num = int(float('2.5'))
print(num)

num = float('1.5')
print(num*2)

num = str(2)
print(num*2)
#------------------------------------------------------------------------------
# (7) 연산자
#       산술연산자  : 더하기 +,   빼기 -,  곱하기 *,   나누기 /
print(5+2)   #---> 7
print(5-2)   #---> 3
print(5*2)   #---> 10
print(5/2)   #---> 2.5
#                   나머지 %,   몫 //,   거듭제곱 **
print(5%2)   #---> 1
print(5//2)  #---> 2
print(5**2)  #---> 25
print(5**3)  #---> 125
#       비교연산자  : 크다 >, 크거나같다 >=, 작다 <, 작거나같다 <=
print(5>2)   #---> True
print(5>=2)  #---> True
print(5<2)   #---> False
print(5<=2)  #---> False
#                    같다 ==, 같지않다 !=
print(5==2)  #---> False
print(5!=2)  #---> True
#       논리연산자  : 둘다참이면 True - and, 하나라도참이면 True - or, 반전 not
print(3<5 and 7<5)   #---> False
print(3<5 or 7<5)    #---> True
print(not 3<5)       #---> False
#       멤버연산자  : 포함 in, 미포함 not in
print('c' in 'cat')     #---> True
print('c' not in 'cat') #---> False
#
# '22.07.20 21:30 종료

#------------------------------------------------------------------------------
# '22.07.23 23:31 시작
# (8) 불리안
#       불리안으로 형변환   : bool()
#                           값이 있으면 True, 없으면 False
#                           a = "hello", b = " " 는 값이 있는것, c = ""는 값이 없는 것
#                           a = 1, a = -2는 값이 있는것, c = 0은 값이 없는 것
#                           None 값이 없는 것
a = "hello"
b = "   "
c = ""
d = 1
e = -2
f = 0
g = None

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))

#------------------------------------------------------------------------------
# (9) 주석
#   #을 붙이면 한줄을 주석 처리
''' 따옴표 세개 쓰면
여러줄에 걸쳐서 주석 처리'''

#------------------------------------------------------------------------------
# (10) 인덱스와 슬라이싱
#   몇번째 = 인덱스
#   첫번째가 1이 아니라 0부터 시작

lang = "PYTHON"

# 인덱스가
#        P  Y  T  H  O  N
#        0  1  2  3  4  5
#       -6 -5 -4 -3 -2 -1

print(lang[0]) #인덱스가 0이니깐 첫번째 글자가 나온다
print(lang[5]) #인덱스가 5이니깐 여섯번째 글자가 나온다
print(lang[-1]) #마지막을 -1로 할수 있다

# 슬라이싱
print(lang[1:6]) # 1부터 5까지는 [1:끝인덱스+1]
print(lang[3:]) #끝까지 자르려면 콜론뒤에 안쓰면된다
print(lang[:3]) #처음부터 하려면 콜론 앞에 안쓰면 된다
print(lang[:]) #처음부터 끝까지는 콜론만 쓰면 된다.

#------------------------------------------------------------------------------
# (11) 문자열 처리
#       [1] 문자열 더하기

snack = '꿀꽈배기'
two = '2개'
juseyo = snack + two
print(juseyo)

juseyo += '주세요' # juseyo = juseyo + '주세요' 이렇게 써도 되는데, juseyo가 두번쓰였음. 간단히 하기 위해 +=로 쓸 수 있다.
print(juseyo)

#       [1-1] 자기 스스로에 더하기, 빼기, 곱하기, 나누기 연산하기
num = 3
num = num + 2
num += 2  #위 문장과 동일함

num = num - 1
num -= 1  #위 문장과 동일함

num *= 2
num /= 4

#       [2] 문자열 길이 구하기
print(len(snack)) # len 함수는 문자열의 길이를 구한다

#       [3] 여러줄 문자 쓰기, 문자열 앞뒤로 따옴표 3개로 감싸면 된다
snack_2 = '''꿀꽈배기는
너무
맛있어요'''
print(snack_2)

# '22.07.23 23:58 종료