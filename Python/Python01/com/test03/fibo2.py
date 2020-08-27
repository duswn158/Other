#-*-coding:utf-8*-

# fibonacci 수열 출력하자
def fibo1(n):
    #0 1 1 2 3 5 8
    a, b = 0, 1
    i = 0
    while i < n:
        a,b = b, a+b
        i += 1
    print()

# fibonacci 수열을 list에 담아서 리턴하자.
def fibo2(n):
    a, b = 0, 1
    i = 0
    lst = list()
    while i < n:
        lst.append(a)
        a, b = b, a+ b
        i += 1
    return lst

if __name__=='__main__':
    n = int(input('n :'))
    fibo1(n)
    fibo = fibo2(n)
    print(fibo)