'''
https://codeforces.com/gym/106507/submission/372909469
'''
def solve(n: int, m: int, la: list[list[int]], sa: list[int]) -> bool:
    m0, b0 = la[0]
    if all(m_i == m0 and b_i == b0 for m_i, b_i in la):
        return True
    elif m == 0:
        return True  
    elif m > 1:
        return False  
    xt = sa[0]
    yt = m0 * xt + b0
    for i in range(1, n):
        m, b = la[i]
        if m * xt + b != yt:
            return False
    return True

