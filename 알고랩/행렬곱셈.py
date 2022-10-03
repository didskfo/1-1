def ls(): # 반복적으로 입력받는 것을 함수로 정의
    return list(map(int, input().split()))


n = int(input())
for u in range(n):
    r, s, t = map(int, input().split()) # 행렬의 크기 : rxs, sxt
    x = [] # 첫 번째 행렬
    y = [] # 두 번째 행렬
    z = [] # 결과 행렬
    for i in range(r):
        x.append(ls())
    for i in range(s):
        y.append(ls())
    for i in range(r):
        for j in range(t):
            sum_ = 0
            for k in range(s): # 행렬끼리 곱하기 
                sum_ += x[i][k]*y[k][j]
            z.append(sum_) # 결과값을 결과 행렬에 append
    for i in range(r): # r줄에 
        for j in range(t): # t개씩 
            print(z[0], end=" ") # 출력하기 
            del z[0]
        print()