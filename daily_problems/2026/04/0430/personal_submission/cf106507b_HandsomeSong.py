import sys
input = sys.stdin.readline
def II():
    return int(input())
def LII():
    return list(map(int, input().split()))
t=II()
for _ in range(t):
    n=II()
    a=LII()
    if n==1:
        print(1)
        continue
    cuts = []
    for i in range(n):
        if a[i] == a[(i + 1) % n]:
            cuts.append(i)
    k = len(cuts)
    if k == 0:
        print(1)
        continue
    C_bad = 0
    for j in range(k):
        start = (cuts[j] + 1) % n
        end = cuts[(j + 1) % k]
        if start != end and a[start] == a[end]:
            C_bad += 1
    print(k + C_bad)
