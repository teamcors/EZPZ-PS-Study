import sys
input = sys.stdin.readline

def allocate_budget(budgets, total_budget):
    start, end = 1, max(budgets)
    
    while start <= end:
        mid = (start + end) // 2
        total_allocated = sum(min(budget, mid) for budget in budgets)
        
        if total_allocated > total_budget:
            end = mid - 1
        else:
            start = mid + 1

    return end

N = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

result = allocate_budget(budgets, total_budget)
print(result)
