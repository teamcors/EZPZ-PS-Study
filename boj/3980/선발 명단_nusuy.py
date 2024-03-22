import sys
input = sys.stdin.readline

def dfs(ability, results, result, players, idx):
    if idx == 11:
        results.append(result)
        return
    player = -1
    for j in range(11):
        if ability[j][idx] > 0 and not players[j]:
            player = j
            players[player] = True
            dfs(ability, results, result + ability[j][idx], players, idx + 1)
            players[player] = False

def solution(ability):
    players = [False for _ in range(11)]
    results = []
    dfs(ability, results, 0, players, 0)
    print(max(results))

c = int(input())
result = ''
for j in range(c):
    ability = [[] for _ in range(11)]
    for i in range(11):
        ability[i] = list(map(int, input().split()))
    solution(ability)
