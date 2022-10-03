t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())                              # 사각형 좌표 네개_1
    x, y, z, r = map(int, input().split())                              # 사각형 좌표 네개_2
    if a > z or c < x or d < y or r < b:
        if (x < a < z and x < c < z) and (y < b < r and y < d < r):
            s = (z-x)*(r-y)                                             # s는 면적
            l = (z-x)*2 + (r-y)*2                                       # l은 둘레
        
        elif (a < x <c and a < z < c) and (b < y < d and b < r < d):
            s = (c-a)*(d-b)
            l = (c-a)*2 + (d-b)*2
        else:
            s = (c-a)*(d-b) + (z-x)*(r-y)
            l = (c-a)*2 + (d-b)*2 + (z-x)*2 + (r-y)*2
    
    else:
        li_x = [a, c, x, z]
        li_y = [b, d, y, r]
        li_x.sort()
        li_y.sort()
        s = (z-x)*(r-y) + (c-a)*(d-b) - (li_x[2]-li_x[1])*(li_y[2]-li_y[1])
        l = (li_x[3]-li_x[0] + li_y[3]-li_y[0])*2

    print(s, l)
    a =