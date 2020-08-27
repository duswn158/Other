#-*-coding:utf-8*-

#split
str01 = 'Hello, wod\nHello , pthon'
print(str01)

arr01 = str01.split(' ')
print(arr01)

# [] : list
# {} : set, dictionary
# () : tuple

arr02 = str01.split(' ',2)
print(arr02)

import re
arr03 = re.split("[\s]|[,]", str01)
print(arr03)

# join
arr04 = ['1','2','3','4']
print(arr04)
a = '+'.join(arr04)
print(a)

print(eval(a)) # eval 위험해!