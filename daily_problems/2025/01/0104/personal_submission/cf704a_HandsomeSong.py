import sys
input = sys.stdin.readline
def MII():
    return map(int, input().split())
n, q = MII()
cnt = [0] * (n + 1)
unread = [0] * (n + 1)
stk = []
ans = 0
p = 0
res = []
for _ in range(q):
    t, x = MII()
    if t == 1:
        ans += 1
        cnt[x] += 1
        stk.append(x)
    elif t == 2:
        ans -= cnt[x]
        cnt[x] = 0
        unread[x] = len(stk)  # 这里用 len(stk) 当作时间戳，思路绝了！
    else:
        while p < x:
            if p >= unread[stk[p]]:
                ans -= 1
                cnt[stk[p]] -= 1
            p += 1
    res.append(str(ans))
sys.stdout.write("\n".join(res))