import copy

t = int(input())
for i in range(t):
    n, k = map(int, input().split()) # n은 격자판 크기, k는 시간 
    x = list(map(int, input().split()))
    x.insert(0,0) # 맨 앞에 0 추가해줌
    x.append(0) # 맨 뒤에 0 추가해줌
    x__ = x[u-1] + x[u+1]                   
    for j in range(k):
        y = copy.deepcopy(x) # 값 바꿀 리스트 카피함
        for u in range(1, n+1):
            if x__ < 3 or x__ > 7: # 한 마리 죽는 경우 = 양 옆 합이 3보다 작거나 7보다 클 때
                if y[u] > 0: # 개수가 음수가 되면 안되니까 
                    y[u] = y[u] - 1
            elif 4 <= x__ <= 7: # 한 마리 생기는 경우 = 4마리와 7마리 사이
                if y[u] < 9: # 9마리 넘으면 안되니까 
                    y[u] = y[u] + 1
            elif x__ == 3: # 변화 없는 경우 = 양 옆 합이 3일 때
                pass 
        x = y # 바꾼 리스트를 출력할거임
    for u in range(1, n+1):
        print(x[u], end=" ")
    print()
