import sys
from collections import defaultdict

def solution():
    y, x = map(int, input().split())
    words = [''] * x
    for _ in range(y):
        new_words = list(sys.stdin.readline().rstrip())
        words = [''.join(x) for x in zip(words, new_words)]
    
    count = 0
    for start in range(1, y):
        data = defaultdict(int)
        for s in words:
            if data[s[start:]] == 0:
                data[s[start:]] += 1
            else:
                return count
        count += 1
    
    return count


if __name__ == '__main__':
    print(solution())
