t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    a = bin(a)[2:] # 이진수로 바꾸기
    b = bin(b)[2:]
    cnt_1 = 0 # a의 해밍무게 세기 위함
    cnt_2 = 0 # b의 해밍무게 세기 위함
    cnt_3 = 0 # 해밍거리 세기 위함

    for k in range(len(a)): # 해밍무게 세는 중
        if a[k] == "1":
            cnt_1 += 1

    for k in range(len(b)): # 해밍무게 세는 중 
        if b[k] == "1":
            cnt_2 += 1

    if len(a) != len(b): # 두 이진수의 길이가 다를 때
        if len(a) > len(b): # a 이진수의 길이가 더 길 때
            b = b.zfill(len(a)) # a 이진수의 길이와 같아지게 b 이진수 앞에 0붙임
        else: # b 이진수의 길이가 더 길 때
            a = a.zfill(len(b)) # b 이진수의 길이와 같아지게 a 이진수 앞에 0붙임

    for j in range(len(a)): # 해밍거리 구하는 중
        if a[j] != b[j]:
            cnt_3 += 1

    print(cnt_1, cnt_2, cnt_3)

    