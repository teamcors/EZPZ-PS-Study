import sys
from collections import defaultdict
input = sys.stdin.readline

visited = {}
ans = []

def dfs(cnt, word):
    global visited, ans
    if cnt == len(word):
        print(''.join(ans))
        return
    
    for v in visited:
        if visited[v]:
            visited[v] -= 1
            ans.append(v)
            dfs(cnt+1, word)
            visited[v] += 1
            ans.pop()


def solution():
    global visited, ans
    n = int(input())
    
    for _ in range(n):
        word = sorted(list(input().rstrip()))
        visited = defaultdict(int)
        ans = []
        
        for c in word:
            visited[c] += 1
        
        dfs(0, word)
    
if __name__ == '__main__':
    solution()