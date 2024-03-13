import sys
input = sys.stdin.readline

def find_cutting_height(trees, target_length):
    start, end = 0, max(trees)
    
    while start <= end:
        mid = (start + end) // 2
        total_length = sum(tree - mid if tree > mid else 0 for tree in trees)
        
        if total_length >= target_length:
            start = mid + 1
        else:
            end = mid - 1

    return end

n, m = map(int, input().split())
trees = list(map(int, input().split()))

result = find_cutting_height(trees, m)
print(result)
