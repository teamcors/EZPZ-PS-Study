# DFS
def dfs(numbers, idx, total, target):
    if idx+1 == len(numbers) and total == target:
        count += 1
        return
    
    for num in numbers[idx:]:
        dfs(numbers, idx + 1, total + num, target)
        dfs(numbers, idx + 1, total - num, target) 

def solution(numbers, target):
    global count
    count = 0
    dfs(numbers, 0, 0, target)
    return count
