    import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = 0, 0
energy = [None]
memo = []

def dp(i, k_avail): # dp: i번째 돌에서 k_avail 상태일 때의 최소 에너지
    global memo
    
    if i == n:
        return 0
        
    if i > n:
        return 100000
        
    if memo[i][k_avail]:
        return memo[i][k_avail]
        
    a, b, c = 0, 0, 100000
    a = dp(i+1, k_avail) + energy[i][0]
    b = dp(i+2, k_avail) + energy[i][1]
    if k_avail:
        c = dp(i+3, False) + k
        
    mn = min(a, b, c)
    
    memo[i][k_avail] = mn
    return mn
    

def solution():
    global n, k, energy, memo
    n = int(input())
    for _ in range(n-1):
        energy.append(list(map(int, input().split())))
    
    memo = [[0 for _ in range(3)] for _ in range(n)]
    k = int(input())
    
    print(dp(1, True))

if __name__ == '__main__':
    solution()