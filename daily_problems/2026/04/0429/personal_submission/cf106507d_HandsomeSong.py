import sys
input = sys.stdin.readline
def II():
    return int(input())
def LII():
    return list(map(int, input().split()))
def MII():
    return map(int, input().split())
t=II()
for _ in range(t):
    n,m=MII()
    kk=[]
    bb=[]
    for _ in range(n):
        k,b=MII()
        kk.append(k)
        bb.append(b)
    s=LII() if m>0 else []
    flag=True
    sing=False
    x,y=0,0
    for i in range(1,n):
        if kk[i]==kk[0]:
            if bb[i]!=bb[0]:
                flag=False
        else:
            sing=True
            x=(bb[0]-bb[i])//(kk[i]-kk[0])
            y=kk[i]*x+bb[i]
    if sing:
        for i in range(n):
            k=kk[i]
            b=bb[i]
            if y!=k*x+b:
                flag=False
    if m:
        for xx in s:
            if sing and xx!=x:
                flag=False
    else:
        flag=True

    print("YES"if flag else "NO")