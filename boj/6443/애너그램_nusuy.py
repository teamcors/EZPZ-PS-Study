import sys
input = sys.stdin.readline

def solution(words):
    values = []

    def dfs(visited, word, value):
        if len(value) == len(word):
            values.append(value)
            return

        prev = ""
        for i in range(len(word)):
            if not visited[i] and prev != word[i]:
                visited[i] = True
                dfs(visited, word, value + word[i])
                visited[i] = False
                prev = word[i]

    for w in words:
        visited = [False for _ in range(len(w))]
        dfs(visited, w, "")
    print("\n".join(values))

n = int(input())
words = ["" for _ in range(n)]
for i in range(n):
    words[i] = sorted(input().rstrip())
solution(words)
