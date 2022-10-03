"""
Problem:
    컴프 10-2
    국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20223103 양나래
"""
import copy

def solution():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        x = list(map(int, input().split()))
        x.insert(0,0)
        x.append(0)
        for j in range(k):
            y = copy.deepcopy(x)
            for u in range(1, n+1):
                if x[u-1] + x[u+1] < 3 or x[u-1] + x[u+1] > 7:
                    if y[u] > 0:
                        y[u] = y[u] - 1
                elif 4 <= x[u-1] + x[u+1] <= 7 :
                    if y[u] < 9:
                        y[u] = y[u] + 1
                elif x[u-1] + x[u+1] == 3:
                    pass
            x = y       
        for u in range(1, n+1):
            print(x[u], end=" ")
        print()


if __name__ == "__main__":
    solution()

# 양옆 합 < 3 외로워서 -1
# 양옆 합 > 7 갑갑해서 -1
# 양옆 합 = 4, 5, 6, 7 활발해서 +1
# 양엽 합 = 3 변화 없음
# 0 < 박테리아 < 9
# 양 옆 끝에 0 추가해서 이웃 만들어주기