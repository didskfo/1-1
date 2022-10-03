import sys

t = int(input())
for i in range(t):
    x = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    m = 0
    for k in range(len(x)-1): # 같은 수가 연속되는거 삭제하기 
        if x[m] == x[m+1]:
            del x[m+1]
        else:
            m += 1

    for j in range(1, len(x)-1):
        if x[j] > x[j-1] and x[j] > x[j+1]: # 양 옆보다 높은 지 확인
            cnt += 1

    print(cnt)