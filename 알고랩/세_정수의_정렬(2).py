"""
Problem:
    세 정수의 정렬(2)
    국민대학교 소프트웨어융합대학 소프트웨어학부 1학년 20223103 양나래
"""

from ntpath import join
from re import A


def solution():
    t = int(input())
    for i in range(t):
        ls = list(map(int, input().split()))
        a = ls[0]
        b = ls[1]
        c = ls[2]
        if a <= b:
            if b <= c:
                ls_a = [a, b, c]
            else:
                if a <= c:
                    ls_a = [a, c, b]
                else:
                    ls_a = [c, a, b]
        else:
            if c <= b:
                ls_a = [c, b, a]
            else:
                if a <= c:
                    ls_a = [b, a, c]
                else:
                    ls_a = [b, c, a]

    print(" ".join(ls_a))



if __name__ == "__main__":
    solution()