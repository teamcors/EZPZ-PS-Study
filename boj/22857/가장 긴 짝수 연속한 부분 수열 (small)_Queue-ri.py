import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    s = [0] + list(map(int, input().split()))
    memo = [[0 for _ in range(k+1)] for __ in range(n+1)]
    
    for i in range(1, n+1):
        s[i] &= 1
        for j in range(k+1):
            if s[i] == 0:
                memo[i][j] = memo[i-1][j] + 1
            if j and s[i]:
                memo[i][j] = memo[i-1][j-1]
                
    res = []
    for i in memo:
        res.append(i[k])
    
    print(max(res))

if __name__ == '__main__':
    solution()