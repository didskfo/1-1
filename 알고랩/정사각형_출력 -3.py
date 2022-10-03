def pnt(x):
    print(x, end="")

t = int(input())
for k in range(t):
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i % (n//2) == 0: 
                if j % (n//2) == 0:
                    if i == j == n//2:
                        pnt("*")
                    else:
                        pnt("+")
                else:
                    pnt("-")
            else:
                if j % (n//2) == 0:
                    pnt("|")
                else:
                    if i == j:
                        pnt("\\")
                    elif i + j == n-1:
                        pnt("/")
                    else:
                        pnt(".")
        print()

a= 