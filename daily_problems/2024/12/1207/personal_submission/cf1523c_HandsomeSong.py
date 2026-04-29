import sys
input = sys.stdin.readline
def II():
    return int(input())
t=II()
out=[]
for _ in range(t):
    n=II()
    stk=[]
    for _ in range(n):
        x=II()
        if x==1:
            stk.append(1)
        else:
            while stk[-1]!=x-1:
                stk.pop()
            stk[-1]=x
        out.append('.'.join(map(str,stk)))
print('\n'.join(out))