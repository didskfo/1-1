"""
Problem:
    오셀로 게임
    국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20223103 양나래
"""
import sys
input = sys.stdin.readline

def solution():
    t = int(input())

    dx = [1,1,1,0,0,-1,-1,-1] # 8방향을 확인할 때 사용할 예정
    dy = [1,0,-1,1,-1,1,0,-1] # 위에랑 같은 이유 
    for i in range(t): # 오셀로 판 개수 
        ls_o = [["+" for i in range(8)] for i in range(8)] # 입력받기
        ls_o[3][3], ls_o[4][4] = "O", "O" # 초기설정
        ls_o[3][4], ls_o[4][3] = "X", "X" # 초기설정
        n = int(input()) 
        a = 0 # 검은돌, 흰돌 번갈아 놓을 때 사용
        o = 0 # 흰돌 개수 
        x = 0 # 검은돌 개수 

        for j in range(n): # 횟수(놓는 돌 개수)
            if a%2 == 0: # 검은돌, 흰돌 번갈아 놓기 위해 설정 
                dol = "X" # 검은돌
            else:
                dol = "O" # 흰돌 
            row, col = map(int, input().split()) # 돌 놓는 위치 
            row = row -1 # 인덱스로 사용하니까 1씩 빼줌
            col = col -1 # 위에랑 같은 이유 
            ls_o[row][col] = dol # 돌 놓는 위치 
            a += 1 # 검은돌, 흰돌 체인지 

            for l in range(8): # 8방 확인하기 
                r = row # row값 r에 저장 
                c = col # col값 c에 저장 
                count = 0 # 몇칸 갔는지 (돌 뒤집을 때 필요)
                needToSwap = False # 돌 뒤집을지 여부

                while 1: # 돌 확인
                    r += dx[l] # 8방 확인
                    c += dy[l] # 위에랑 같음 
                    if r < 0 or r > 7 or c < 0 or c > 7: # 이동했을 때 벽에 부딪히는 경우
                        break
                    elif ls_o[r][c] == "+" : # 이동했을 때 "+" 만난 경우 
                        break
                    elif ls_o[r][c] == dol: # 같은게 나온 경우 
                        needToSwap = True # 돌 뒤집어야됨 
                        break
                    else: # 다른게 나온 경우 
                        count += 1 # 한 칸 더 갈거니까 
                        continue

                if needToSwap: # 돌 뒤집기 
                    # print("count : ",count)
                    # print("r, c : ", r, c)
                    for k in range(count): # 뒤집기
                        r -= dx[l] # 왔던 길 되돌아가기 
                        c -= dy[l] # 위에랑 같음 
                        if ls_o[r][c] == "O": 
                            ls_o[r][c] = "X"
                        elif ls_o[r][c] == "X":
                            ls_o[r][c] = "O"

            # for k in range(8):
            #     print(" ".join(ls_o[k]))
            #     print() 
        
        # 개수 세기 
        for j in range(8):
            for k in range(8):
                if ls_o[j][k] == "O":
                    o += 1
                elif ls_o[j][k] == "X":
                    x += 1

        # 모양 출력
        print(x, o)
        for k in range(8):
            print("".join(ls_o[k]))
            
if __name__ == "__main__":
    solution()