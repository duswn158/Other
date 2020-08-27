# -*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']

for i in subject:
    print(i, end=' ')
else:
    print('재미있다.')

for i in range(1, 100):
    print(i, end='+')

print('\n구구단')
for i in range(2, 10):
    print('<<'+str(i)+"단>>")
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i*j))


for i in range(1, 11):
    print(i, end=' ')
print()

for i in range(10, 0, -1):
    print(i, end=' ')