# 28min 23sec
# 이전 풀이
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

current_sum = nums[0]
max_sum = nums[0]

for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)

#############
# 최적화
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp[i]는 nums[i]를 포함한 최대 연속 부분합을 저장
dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))
