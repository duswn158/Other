# -*- coding:utf-8 -*-



#1. for 문을 사용하여 구구단을 전체 출력하는 함수 gugu()를 작성하고 main 함수에서 호출 하자 .

def gugu():
    for i in range(2,10):
        print('<<%d단>>'%i)
        for j in range(1,10):
            print('%d*%d=%d'%(i,j,i*j))
            print()

#2.while문을 사용하여 구구단 중 파라미터를 전달된 단만 출력하는  함수 gugudan(x)를 작성하고 main 함수에서 
#콘솔을 통해 n을 입력 받아 호출하자 

def gugudan(x):
    print('<<',x,'단>>')
    i=1
    while i<10:
        print('{}*{}={}'.format(x,i,int(x)*i))
        i+=1
        print()
    




if __name__=='__main__':
    a=gugu()
    print(a)
    
    n=input('gugudan : ') #input 자체가 String을 리턴 그래서 함수에서 int 형으로 변환 해야한다.
    gugudan(n)