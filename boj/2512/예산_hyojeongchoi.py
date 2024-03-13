import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(input())

low, high = 0, max(nums)  

answer = 0  
while low <= high:
    total = 0
    mid = (low + high) // 2  

    for num in nums:  
        total += min(num, mid)

    if total <= m:  
        low = mid + 1
        answer = mid
    else:  
        high = mid - 1

print(answer)
