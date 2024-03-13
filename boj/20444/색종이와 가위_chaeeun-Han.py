import sys
input = sys.stdin.readline

def binary_search(n, k):
    start = 0
    end = n // 2

    while start <= end:
        mid = (start + end) // 2
        pieces = (mid + 1) * (n - mid + 1)
    
        if k == pieces:
            return 'YES'
        elif k > pieces:
            start = mid + 1
        else:
            end = mid - 1
        
    return 'NO'

n, k = map(int, input().split())
print(binary_search(n, k))
