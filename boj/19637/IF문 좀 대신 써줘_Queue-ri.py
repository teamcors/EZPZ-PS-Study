import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    title = []
    base = []
    for i in range(n):
        t, b = input().split()
        title.append(t)
        base.append(int(b))
        
    for _ in range(m):
        tc = int(input())
        min_idx = 0
        max_idx = n-1
        ans = -1
        
        while min_idx <= max_idx:
            mid_idx = int((min_idx + max_idx) / 2)
            
            if tc <= base[mid_idx]:
                max_idx = mid_idx - 1
                ans = mid_idx
            else:
                min_idx = mid_idx + 1
        
        print(title[ans])


if __name__ == '__main__':
    solution()
