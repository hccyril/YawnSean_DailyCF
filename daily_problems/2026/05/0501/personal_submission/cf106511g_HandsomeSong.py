import sys
input = sys.stdin.readline
def II():
    return int(input())
t=II()
for _ in range(t):
    n=II()
    chars=[chr(ord('A')+j) for j in range(n)]
    ans=[]
    while n>0:
        if n%2:
            idx=n//2
            ans.append(chars.pop(idx))
            n-=1
        else:
            idx=n//2-1
            ans.append(chars.pop(idx))
            ans.extend(reversed(chars))
            break
    print("".join(ans))