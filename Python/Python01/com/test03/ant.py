#-*-coding:utf-8*-

'''

1 1
1 2
1 1 2 1
1 2 2 1 1 1
1 1 2 2 1 3 
1 2 2 2 1 1 3 1
1 1 2 3 1 2 3 1 1 1

'''

def ant(i):
    
    # 1 기준 -> 몇개?
    # 2가 나오면 1기준으로 몇개가 있었는지 결과에 추가
    # 2 기준 -> 몇개?
    # 1이 나오면 2기준으로 몇개가 있었는지를 결과에 추가
    # 1 기준 -> 몇개?
    # 결과에 추가
    # 리턴
    inp = str(i)
    target = inp[0]
    cnt = 0
    res = ''
    for a in inp:
        if a == target:
            cnt += 1
        else:
            res += target + str(cnt)
            cnt = 1
            target = a
    res += target + str(cnt)
    return res


if __name__ == '__main__':
    n = int(input('ant stage : '))
    val = ant(1)
    
    print('1')
    for i in range(1, n):
        val = ant(val)
        print(val)
        