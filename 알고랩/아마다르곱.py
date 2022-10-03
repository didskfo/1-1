t = int(input())
for k in range(t):
    r, s = map(int, input().split())
    x = []
    y = []
    
    for i in range(r):
        x.append(list(map(int, input().split())))

    for i in range(r):
        y.append(list(map(int, input().split())))

    for j in range(r):
        for k in range(s):
            print(x[j][k]*y[j][k], end=" ") # 행렬의 같은 위치에 있는 원소들끼리 곱한 값을 출력 
        print()