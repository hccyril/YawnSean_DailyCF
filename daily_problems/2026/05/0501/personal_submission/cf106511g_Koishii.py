fact = [1] * 27
for i in range(1, 27):
    fact[i] = fact[i - 1] * i


outs = []
for _ in range(int(input())):
    n = int(input())
    m = (fact[n] + 1) // 2
    vis = [False] * n
    now = 1
    ans = []
    for i in range(n):
        rk = n - i
        for j in range(n - 1, -1, -1):
            if vis[j]: continue
            ne = now + fact[n - i - 1] * (rk - 1)
            rk -= 1
            if ne <= m:
                now = ne
                ans.append(chr(j + 65))
                vis[j] = True
                break

    outs.append(''.join(map(str, ans)))

print('\n'.join(map(str, outs)))
