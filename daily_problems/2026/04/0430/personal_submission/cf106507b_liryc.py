'''
https://codeforces.com/gym/106507/submission/373039179
'''
def solve(n: int, a: list) -> int:
    if n == 1:
        return 1
    ia = [i for i in range(n) if a[i] == a[i - 1]]
    if not ia:
        return 1
    elif len(ia) == 1: 
        return 2
    nc = len(ia)
    for i, j in pairwise(ia):
        if j - i > 1 and a[i] == a[j - 1]: 
            nc += 1
    i, j = ia[-1], ia[0]
    if j + n - i > 1 and a[i] == a[j - 1]:
        nc += 1
    return nc
