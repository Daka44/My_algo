import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = int(input())
    if int(x**(1/2)) ** 2 == x:
        print(1)
    else:
        print(0)