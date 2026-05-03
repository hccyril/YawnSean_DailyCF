import sys
input = sys.stdin.readline
def II():
    return int(input())
def MII():
    return map(int, input().split())
t=II()
for _ in range(t):
    n,m=MII()
    if n == 1 and m == 1:
        print(1)
    elif n == 1 or m == 1:
        print(2)
    elif n != m:
        print(4)
    else:
        print(8)
