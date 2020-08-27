#-*-coding:utf-8*-

# cmd 창에서 아래 명령어 입력
# pip install numpy
# pip install matplotlib

# warning이라고 버젼 다르다고 나오는데 '' 안에 있는 경로부터 명령어까지 복사해서 명령어입력

import numpy as np
import matplotlib.pyplot as plt
import random

def plt01():
    x = np.arange(0, 11)
    y = x
    
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['y=x'])
    plt.show()


def plt02():
    y = [random.randint(0, 10) for i in range(10)]
    x = range(10)
    plt.bar(x, y)
    plt.xticks(range(11))
    plt.yticks(range(11))
    plt.show()


if __name__ == '__main__':
    #plt01()
    plt02()