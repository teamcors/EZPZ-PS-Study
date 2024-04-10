import sys
input = sys.stdin.readline
    
def solution():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        memo = [list(map(int, input().split())) for _ in range(2)]
        
        if n > 1 :
            memo[0][1] += memo[1][0]
            memo[1][1] += memo[0][0]
        
        for i in range(2, n):
            memo[0][i] += max(memo[1][i-1], memo[1][i-2])
            memo[1][i] += max(memo[0][i-1], memo[0][i-2])
    
        print(max(memo[0][n-1], memo[1][n-1]))

if __name__ == '__main__':
    solution()