import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    dots = map(int, input().split())
    dots = sorted(dots)
    
    left, right = -1, -1
    for tc in range(m):
        a, b = map(int, input().split())
        
        min_idx, max_idx = 0, len(dots)-1
        
        # find the left end idx
        while min_idx <= max_idx:
            mid_idx = int((min_idx + max_idx) / 2)
            
            if a <= dots[mid_idx]:
                max_idx = mid_idx - 1
                left = mid_idx
            else:
                min_idx = mid_idx + 1
        
        min_idx, max_idx = 0, len(dots)-1
        
        # find the right end idx
        while min_idx <= max_idx:
            mid_idx = int((min_idx + max_idx) / 2)
            
            if dots[mid_idx] <= b:
                min_idx = mid_idx + 1
                right = mid_idx
            else:
                max_idx = mid_idx - 1
                
        if b < dots[left] or dots[right] < a:
            print(0)
        else:
            print(right - left + 1)

if __name__ == '__main__':
    solution()
