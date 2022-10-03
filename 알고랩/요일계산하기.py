t = int(input())
for i in range(t):
    y, m, d = map(int, input().split()) # 년, 월, 일 입력받기
    cnt = 0 # 총 날짜 구할거 
    for i in range(1, y): # 윤년 판별해서 연도까지에 해당되는 날짜 구하기
        if (i % 400 == 0) or ((i % 4 == 0) and (not (i % 100 == 0))):
            cnt += 366
        else:
            cnt += 365
    # print(cnt)
    cnt = cnt % 7 # 너무 큰 수니까 미리 한 번 나눠주기
    if (y % 400 == 0) or ((y % 4 == 0) and (not (y % 100 == 0))): # 윤년에 따라 월에 해당되는 날짜 구하기 
        month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        cnt += sum(month[1:m])
    else:
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        cnt += sum(month[1:m])

        cnt += int(d) # 날짜 더하기 

        print(cnt % 7) # 7로 나눔 