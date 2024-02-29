from collections import defaultdict

def solution():
    data = defaultdict(int)
    str = input()
    
    for length in range(1, len(str)+1):
        for i in range(0, len(str)-length+1):
            data[str[i:i+length]] += 1
    
    print(len(data.keys()))


if __name__ == '__main__':
    solution()
