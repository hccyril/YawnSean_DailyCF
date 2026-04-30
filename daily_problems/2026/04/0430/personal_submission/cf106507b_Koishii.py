outs = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    last = -1
    first = -1
    for i in range(n):
        if a[i] == a[(i + 1) % n]:
            cnt += 1
            if first == -1:
                first = i
            if last != -1 and a[last] == a[i] and last != i:
                cnt += 1
            last = (i + 1) % n

    if last != -1 and first != -1 and a[last] == a[first] and first != last:
        cnt += 1

    if cnt == 0 or n == 1:
        outs.append(1)
    else:
        outs.append(max(cnt, 2))


print('\n'.join(map(str, outs)))
