# Submission link: https://codeforces.com/gym/106507/submission/372916758
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        idx = -1
        ans = 0
        
        for i in range(n):
            if nums[i] == nums[i - 1]:
                idx = i
                ans += 1
        
        if ans == 0 or n == 1: outs.append(1)
        else:
            cur_idx = idx
            for i in range(1, n + 1):
                if nums[(idx + i) % n] == nums[(idx + i - 1) % n]:
                    if cur_idx != idx + i - 1 and nums[cur_idx % n] == nums[(idx + i - 1) % n]:
                        ans += 1
                    cur_idx = idx + i
            
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))