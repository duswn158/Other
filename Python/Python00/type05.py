# set

# 생성자 사용
a = set(['1','2','3','4','4'])
print(a)

# iterable 하다.= 순서대로 값을 하나씩 가지고 올 수 있다
# 생성자에 iterable한 객체(sequance)를 넣으면
# set의 값으로 각각 분리되어 들어감.
b = set('hello')
print(b)

#{}
c = {'a','b','c','hello','1','2','3'}
print(c)

c.add('world')
print(c)

# 합집합, 교집합
#교집합
print(a.union(b))
print(a | b)

#합집합
print(a.intersection(c))
print(a & c)
