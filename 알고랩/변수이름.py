t = int(input())
for i in range(t):
    a = input()
    pan = 0
    
    for j in range(len(a)):
        if a[0] == "_" or a[0].isalpha(): # 첫 번째 문자가 영문자나 "_"인지 확인 
            if a[j].isalnum() or a[j] == "_": # 영문자나 숫자, "_"로 이루어져 있는지 확인
                pan += 0
            else:
                pan += 1
        else:
            pan += 1

    if pan > 0:
        print(0)
    else:
        print(1)
    

# 첫 번째 문자는 영문자나 "_"만 가능
# 영문자, 숫자, "_"만 가능 