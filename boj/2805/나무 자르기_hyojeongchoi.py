import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(lst)  
while start <= end:
    sum = 0
    mid = (start + end) // 2  

    for l in lst:
        if l > mid:
            sum += l - mid  
    
    if sum < m:  
        end = mid - 1  
    else:  
        start = mid + 1  

print(end)  
