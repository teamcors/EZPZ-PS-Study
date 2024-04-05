def solution(N, number):
    arr = [[]] + [[int(str(N) * i)]for i in range(1, 9)]

    if [number] in arr:
        return arr.index([number])

    for i in range(2, 9):
        for j in range(1, i):
            for a in arr[j]:
                for b in arr[i - j]:
                    arr[i].append(a + b)
                    arr[i].append(a * b)
                    arr[i].append(a - b)
                    if 0 != b:
                        arr[i].append(a // b)
        if number in arr[i]:
            return i
        arr[i] = list(set(arr[i]))

    return -1
