t = int(input())
for i in range(t):
    a, b, c, d = map(int,input().split()) # 네 정수 입력받음
    if c > a and c < b: # 모든 경우의 수 구함
        if  b >= d: # ruq은 겹치는 구간길이 
            ruq = d-c # chd은 총 구간길이 
            chd = b-a 
        else:
            ruq = b-c 
            chd = d-a
        
    elif c > a and c >= b:
        ruq = 0 
        chd = d-c + b-a 

    elif c == a:
        if b >= d:
            ruq = d-c 
            chd = b-a 
        else:
            ruq = b-c 
            chd = d-c 
    
    elif c < a and d <= a:
        ruq = 0
        chd = d-c + b-a 
    
    elif c < a and d > a:
        if d < b:
            ruq = d-a 
            chd = b-c 
        elif d >= b:
            ruq = b-a 
            chd = d-c 
    print(ruq, chd) 