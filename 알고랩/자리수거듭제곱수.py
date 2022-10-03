t = int(input())
for i in range(t):
    a = input()
    b = 0
    for i in range(len(a)): # a의 길이만큼
        b += int(a[i])**int(len(a)) # a의 각 자리에 길이만큼을 곱함
    if b == int(a): # 각 자리에 자리수를 제곱한 값을 더한 값이 원래 값과 같으면 1 출력
        print(1)
    else: # 아니면 0 출력
        print(0)