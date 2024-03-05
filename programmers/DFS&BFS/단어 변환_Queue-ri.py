from collections import deque, defaultdict

def ok(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    
    return diff == 1
    
def solution(begin, target, words):
    adj = defaultdict(list)
    visited = defaultdict(bool)
    words.append(begin)
    n = len(words)
    for i in range(n):
        visited[words[i]] = False
        for j in range(i+1, n):
            if ok(words[i], words[j]):
                adj[words[i]].append(words[j])
                adj[words[j]].append(words[i])
    
    q = deque()
    q.append((begin, 0))
    visited[begin] = True
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        
        for nxt_word in adj[word]:
            if not visited[nxt_word]:
                q.append((nxt_word, cnt+1))
                visited[nxt_word] = True
    
    return 0
