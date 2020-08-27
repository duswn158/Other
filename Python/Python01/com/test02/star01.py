# -*- coding:utf-8 -*-

'''
*
**
***
****
*****
'''

for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
    
for i in range(5):
    print('*' * (i + 1))

'''
*****
****
***
**
*
'''

for i in range(5):
    print('*' * (5 - i))

'''
    *
   **
  ***
 ****
*****
'''

for i in range(5):
    print(' ' * (4 - i) + '*' * (i + 1))

'''
*****
 ****
  ***
   **
    *
'''

for i in range(5):
    print(' ' * (i) + '*' * (5 - i))

'''
    *
   ***
  *****
 *******
*********
'''

for i in range(5):
    print(' ' * (4 - i) + '*' * (2 * i + 1))