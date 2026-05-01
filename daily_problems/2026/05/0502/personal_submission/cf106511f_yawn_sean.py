# Submission link: https://codeforces.com/gym/106511/submission/373233354
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        
        if n == 1 and m == 1: outs.append('1')
        elif n == 1 or m == 1: outs.append('2')
        elif n != m: outs.append('4')
        else: outs.append('8')
    
    print('\n'.join(outs))