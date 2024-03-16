import sys

input = sys.stdin.readline


def solution():
    m, n, l = map(int, input().split())
    shot_pos = list(map(int, input().split()))
    animals = [(0, 0) for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        animals[i] = (x, y)

    shot_pos.sort()
    answer = 0
    for animal in animals:
        a_x, a_y = animal
        left, right = 0, m - 1
        r1, r2 = a_x + a_y - l, a_x - a_y + l
        while left <= right:
            mid = (left + right) // 2

            if r1 <= shot_pos[mid] <= r2:
                answer += 1
                break
            elif shot_pos[mid] < r1:
                left = mid + 1
            else:
                right = mid - 1
    print(answer)


if __name__ == "__main__":
    solution()
