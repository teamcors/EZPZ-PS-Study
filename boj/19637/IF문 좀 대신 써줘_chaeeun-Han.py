#38min 34sec
import sys
input = sys.stdin.readline

def binary_search(target):
    start = 0
    end = n-1 

    while start <= end:
        mid = (start + end) // 2
        
        if nums[mid] < target:
            start = mid + 1
        else: end = mid - 1
    return names[end + 1]
    
n, m = map(int, input().split())
names, nums = [], []

for _ in range(n):
    name, value = input().split()
    names.append(name)
    nums.append(int(value))
    
for _ in range(m):
    target = int(input())
    print(binary_search(target))
