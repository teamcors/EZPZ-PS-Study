from collections import deque, defaultdict

def dfs(adj, cur, depth, max_depth):
    path = []
    
    if depth == max_depth:
        return [cur]
    
    candidate = []
    nxt_lst = [nxt for nxt in adj[cur]]
    for nxt in nxt_lst:
        adj[cur].remove(nxt)
        nxt_path = dfs(adj, nxt, depth+1, max_depth)
        adj[cur].append(nxt)
        
        # path exists
        if len(nxt_path) == max_depth - depth:
            candidate.append(nxt_path)
    
    # 가장 순서가 앞서는 path의 인덱스
    if candidate:
        idx = 0
        for i in range(1, len(candidate)):
            idx = i if candidate[i][-1] < candidate[idx][-1] else idx

        path = candidate[idx]
        path.append(cur)
    
    return path

def solution(tickets):
    adj = defaultdict(list)
    visited = defaultdict(bool)
    for t in tickets:
        adj[t[0]].append(t[1])
    
    ans = dfs(adj, 'ICN', 1, len(tickets)+1)
    ans.reverse()
    return ans
