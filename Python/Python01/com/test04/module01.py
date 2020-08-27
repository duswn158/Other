#-*-coding:utf-8*-

# math 라는 midule을 가져온다
# import math

# math에서 pi만 가져온다.
from math import pi

def circle(x):
    # pi * r * r
    return pi * r * r

if __name__ == '__main__':
    r = int(input('원의 반지름 : '))
    print('반지름이 {}인 원의 넓이는 {} 입니다.'.format(r, circle(r)))