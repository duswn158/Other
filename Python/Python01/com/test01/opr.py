#-*-coding:utf-8*-
from _ast import In

# 산술연산
a = 21
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a**b) #a의 b제곱
print(a / b)
print(a // b) # 나누고 나머지 제거, 즉 몫(floore division - 소수점 이하는 버린다.)
print(a%b)# 나머자ㅣ(modulo)

#비교연산
a,b = 3,5 # a에는 3 b에는 5가 들어감
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)

print('-------------')
print(True or False)
print(False and True)
print(not False)

# 범위연산
lst = list(range(100))
print(lst)
print(lst[2])
print(lst[12 : 49]) # 12~48까지 잘림
print(lst[12:49:3])

#[start : end] -> start ~ end-1
#[start: end: step] -> start ~ end 1 까지 step만큼씩

# 순서가 있는 객체가 됨
str01 = "Hello, World!"
print(str01)
print(str01[0])
print(str01[0:5])
print(str01[6:11])
print(str01[0: 4] * 4)


#reverse
print(str01[-1])
print(str01[-1 : ])
print(str01[: -1])
print(str01[:: -1])

# 멤버연산
lst02 = [0,1,2,3,4,5]
print(3 in lst02) # true
print(5 not in lst02) #false
print(7 not in lst02) # True