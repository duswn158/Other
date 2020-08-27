#-*-coding:utf-8*-

import re # 정규식 모듈

'''

Regular Expression

. : 문자 1개
^ : 문자열의 시작
$ : 문자열의 마지막
[] : 문자 집합
| : or
() : 괄호 안 정규식 그룹

* : 0 or more
+ : 1 ore more
? : 0 or 1
{n} : n번 반복
{n, m} : n번부터 m번
{n, } : n번부터 무한대

'''

"""
r문자열 표기법(re 모듈의 확장 문법)
\w : [a-zA-Z0-9_] : a~z, A~Z, 0~9, _를 포합하는 모든 문자
\w : [^a-zA-Z0-9] : 위의 문자를 제외한 나머지 문자
\d : [0-9] : 0 ~ 9
\D : [^0-9] : 숫자를 제외한 나머지 문자
\s : [\t\n\r\f\v] : 공백문자
\S : [^\t\n\r\f\v] : 공백문자 제외한 나머지 문자
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[n] : 지정된 n만큼 일치하는 문자열
\A : 문자열의 시작
\Z : 문자열의 끝

"""

str01 = '나의 이메일은 kh23213@kh.com123 입니다'
match = re.search(r'[\w]*@[a-zA-Z.]*', str01)
print(match.group())