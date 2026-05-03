import math
import sys
input = sys.stdin.readline
def II():
    return int(input())
k=II()
if k==0:
    print(4)
    print(1,2,3,4)
else:
    a=1
    while a*(a-1)*(a-2)//6<=k:
        a+=1
    a-=1
    k-=a*(a-1)*(a-2)//6
    ans=[0]*a
    cur=1
    while k:
        v=math.isqrt(k)
        ans.append(4*cur)
        ans+=([-3*cur]*v)
        ans+=([-cur]*v)
        k-=v*v
        cur*=10
    print(len(ans))
    if ans: print(*ans)