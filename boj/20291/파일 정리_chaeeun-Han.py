n = int(input())
fileName = [input().split('.') for _ in range(n)]

hash = {}

for l in fileName:
    hash[l[1]] = hash.get(l[1], 0) + 1

sorted_hash = sorted(hash.items())

for x in sorted_hash:
    print(x[0], x[1])
