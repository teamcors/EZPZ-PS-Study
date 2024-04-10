def solution(m, n, puddles):
    memo = [[0] * (m+1) for _ in range(n+1)]
    memo[1][1] = 1
    
    for x, y in puddles:
        memo[y][x] = -1
        
    for y in range(1, n+1):
        for x in range(1, m+1):
            if memo[y][x] == -1:
                memo[y][x] = 0
                continue
            memo[y][x] += (memo[y-1][x] + memo[y][x-1]) % int(1e9+7)
            
    return(memo[n][m])