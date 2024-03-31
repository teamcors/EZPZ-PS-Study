# 52min 34sec
def solution(m, n, puddles):
    dp = [[-1]*(m+1) for _ in range(n+1)]

    for col, row in puddles:
        if row == 1:
            for c in range(col, m+1):
                dp[row][c] = 0
        elif col == 1:
            for r in range(row, n+1):
                dp[r][col] = 0
        dp[row][col] = 0

    for row in range(1, n+1):
        for col in range(1, m+1):
            if dp[row][col] == 0:
                continue
            elif col == 1 or row == 1:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[-1][-1] % 1000000007
