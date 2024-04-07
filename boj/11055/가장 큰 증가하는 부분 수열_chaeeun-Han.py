# 51min 24sec
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [i for i in nums]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))
