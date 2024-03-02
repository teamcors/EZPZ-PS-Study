import sys

hash = {}
cnt = 0

while True:
    data = sys.stdin.readline().rstrip()

    if data == '':
        break

    hash[data] = hash.get(data, 0) + 1
    cnt += 1

sorted_hash = dict(sorted(hash.items()))
for k, v in sorted_hash.items():
    per = (v/cnt * 100)
    print("%s %.4f" % (k, per))
