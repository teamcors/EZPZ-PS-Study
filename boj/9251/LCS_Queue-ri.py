import sys
    
def solution():
    s1 = input()
    s2 = input()
    memo = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    
    for y in range(1, len(s1)+1):
        for x in range(1, len(s2)+1):
            if s1[y-1] == s2[x-1]:
                memo[y][x] = memo[y-1][x-1] + 1
            else:
                memo[y][x] = max(memo[y-1][x], memo[y][x-1])
    
    print(memo[-1][-1])

if __name__ == '__main__':
    solution()