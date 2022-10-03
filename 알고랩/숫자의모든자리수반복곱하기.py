t = int(input()) 
for i in range(t):
    n = input()
    if len(n) > 1: # n의 길이가 1보다 클 때
        while len(n) > 1: # n의 길이가 1보다 큰동안
            x = ""
            a = 1
            for i in range(len(n)): # n 한자리씩 돌기 
                if n[i] != '0': # 그 숫자가 0이 아닐 때 
                    x += n[i] # x에 더하기 
            for j in range(len(x)): # x 한자리씩 돌기 
                a = a*int(x[j]) # x 각 자리끼리 곱하기 위해 
            n = str(a)
        print(n)
    else:
        print(n)
