C = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(ix()):
    n = ix()
    s = C[:n][::-1]
    if n % 2:
        ans = s[n // 2: n // 2 + 2] + s[: n // 2] + s[n // 2 + 2:]
    else:
        ans = s[n // 2] + s[: n // 2] + s[n // 2 + 1:]
    print(ans)
