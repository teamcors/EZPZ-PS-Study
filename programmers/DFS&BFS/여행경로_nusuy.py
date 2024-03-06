from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)

    for a, b in sorted(tickets, key=lambda x: x[1]):
        graph[a].append(b)

    route = []

    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        route.append(start)

    dfs("ICN")
    return route[::-1]
