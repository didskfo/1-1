t = int(input())
for u in range(t):
    n = int(input())
    for i in range(n): # 세로줄 개수
        for j in range(n): # 가로줄 개수
            if i == n//2 and j == n//2: # n을 2로 나눈 몫일 때
                print(0,end="") # 0 출력
            elif max(abs(n//2-i), abs(n//2-j))%2 == 1: # n을 2로 나눈 몫에서 i를 뺀 값과 j를 뺀 값 중에 큰 값의 절댓값이 1일 때 
                print(1,end="") # 1 출력
            else: # 나머지
                print(0,end="") # 0 출력
        print()