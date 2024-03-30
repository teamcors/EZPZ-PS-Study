# 53min 57sec
import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
dp = [1] * n

# lines[][0]에 대하여 정렬
lines.sort()

# LIS 알고리즘을 이용하여 최대 전깃줄 개수 찾기
for i in range(1, n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

# 전체 전깃줄 개수에서 최대 전깃줄 개수를 빼서 없애야 하는 최소 전깃줄 개수 계산
print(n - max(dp))
