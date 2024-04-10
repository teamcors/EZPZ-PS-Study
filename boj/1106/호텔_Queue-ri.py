import sys
input = sys.stdin.readline
    
def solution():
    c, n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = int(1e9)
    memo = [int(1e9)] * (c+100)
    memo[0] = 0
    
    for cost, cstmrs in data:
        for i in range(cstmrs, len(memo)) :
            memo[i] = min(memo[i-cstmrs] + cost, memo[i])
            if i >= c:
                ans = min(ans, memo[i])
    print(ans)

if __name__ == '__main__':
    solution()