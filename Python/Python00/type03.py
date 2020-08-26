# list

# 생성자 사용
a = list()
print(a)
a.append(1)
print(a)
a.append('a')
print(a)
a[0] = 3
print(a)

# a[2] = 5 -> 없는 번지수에 추가할 수 없음
#print(a)

a.append(3)
print(a)

# []사용
b = [1,2,3,4,5]
print(b)

# b 안에 있는 숫자 2와 4를 더해서 출력
print(b[1] + b[3])

b.reverse()
print(b)

b.sort()
print(b)

c = ['a','b','c','d',['e','f','g'],'h']
print(c)
print(c[4])

d = b + c
print(d)

print(c + b)
