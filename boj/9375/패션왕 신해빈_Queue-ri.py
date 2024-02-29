from collections import defaultdict

def solution():
    k = int(input())
    data = defaultdict(int)
    
    for i in range(k):
        type = input().split()[1]
        data[type] += 1
    
    val = list(data.values())
    ans = 1
    for i in val:
        ans *= (i+1)
    
    print(ans - 1)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        solution()
