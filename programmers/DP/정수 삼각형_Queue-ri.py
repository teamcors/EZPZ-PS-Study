def solution(triangle):
    n = len(triangle) - 1
    while n > 0:
        for i in range(n):
            triangle[n-1][i] += max(triangle[n][i], triangle[n][i+1])
        n -= 1
    
    return triangle[0][0]