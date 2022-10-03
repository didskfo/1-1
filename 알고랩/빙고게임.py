t = int(input())
for i in range(t):
    ls = [list(map(int, input().split())) for j in range(5)] # 빙고 입력받기
    num = list(map(int, input().split())) # 숫자 부르는거 입력
    ls[2][2] = -1 # 가운데는 이미 되어있음 / 해당되는 수는 -1로 바꿈 
    for k in range(len(num)):
        x_ = []
        y_ = []

        for u in range(5):
            for q in range(5):
                if ls[u][q] == num[k]: # 불린 숫자는 네모처리
                    ls[u][q] = -1 # 네모처리 : -1

        for u in range(5):
            x = 0 
            for q in range(5):
                x += ls[u][q] # 한 줄에 있는 숫자들을 더하기 - 가로 
            x_.append(x) # 한 줄에 있는 숫자들을 더한 값을 리스트에 추가

        for u in range(5):
            y = 0
            for q in range(5):
                y += ls[q][u] # 한 줄에 있는 숫자들을 더하기 - 세로 
            y_.append(y)

        if -5 in x_ or -5 in y_: # 한 줄에 있는 숫자들 더한 값 중에 -5 있나 확인/-5 : 빙고 의미 
            print(k+1)
            break

        z = ls[0][0] + ls[1][1] + ls[2][2] + ls[3][3] + ls[4][4] # 대각선 값 더하기 
        if z == -5:
            print(k+1)
            break
        r = ls[0][4] + ls[3][1] + ls[2][2] + ls[1][3] + ls [4][0] # 반대 대각선 값 더하기 
        if r == -5:
            print(k+1)
            break
        if ls[0][0] + ls[4][4] + ls[0][4] + ls[4][0] == -4: # 모서리 값 더하기 
            print(k+1)
            break