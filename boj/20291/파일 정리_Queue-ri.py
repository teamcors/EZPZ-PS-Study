from collections import defaultdict

def solution():
    n = int(input())
    data = defaultdict(int)
    for i in range(n):
        ext = input().split('.')[1]
        data[ext] += 1
        
    ans = sorted(data.items())

    for k, v in ans:
        print(k, v)


if __name__ == '__main__':
    solution()
