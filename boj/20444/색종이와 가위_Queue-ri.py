import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    # 한 방향(a)으로 자르는 횟수를 mid로 정의
    # 크로스되는 다른 방향(b)은 자동으로 n-mid번이 됨
    mn, mx = 0, n//2
    while mn <= mx:
        a = (mn + mx) // 2
        b = n - a
        parts = (a+1) * (b+1)
        
        if parts == k:
            print('YES')
            return
        
        if parts < k:
            mn = a + 1
        else:
            mx = a - 1
    
    print('NO')
    
if __name__ == '__main__':
    solution()
