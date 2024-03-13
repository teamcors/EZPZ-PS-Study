import sys
input = sys.stdin.readline

def count_lansens(lansens, target_length):
    count = 0
    for lansen in lansens:
        count += lansen // target_length
    return count

def binary_search_lansens(lansens, required_count):
    left, right = 1, max(lansens)
    
    while left <= right:
        mid = (left + right) // 2
        count = count_lansens(lansens, mid)
        
        if count >= required_count:
            left = mid + 1
        else:
            right = mid - 1

    return right

K, N = map(int, input().split())
lansens = [int(input()) for _ in range(K)]

result = binary_search_lansens(lansens, N)

print(result)
