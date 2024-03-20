import sys
input = sys.stdin.readline

N, ans = 0, 0
S = []

def dfs(start, depth, current_score):
    global ans, min_diff
    ans = min(ans, abs(current_score))
    
    if depth == N // 2:
        return

    for i in range(start, N):
        opponent = sum([S[j][i] + S[i][j] for j in range(N)])
        dfs(i + 1, depth + 1, current_score - opponent)

def solution():
    global N, S, ans
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = sum([sum(S[i]) for i in range(N)])
    
    dfs(0, 0, ans)
    print(ans)
    
if __name__ == '__main__':
    solution()