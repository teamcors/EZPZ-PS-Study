# 50min 27sec
# 1. 구현으로 풀려고 했으나 실패
# 2. dfs로 접근
###############이전 풀이 방식##################
# n = int(input())
# parents = list(map(int, input().split()))
# delnode = int(input())
# graph = [[] for _ in range(n)]

# # 노드 지우기
# parents[delnode] = -2
# for i in range(0, len(parents)):
#     # root 가 -2이면 본인을 -2로 바꾸자
#     if parents[i] == -2 or -2 in graph[parents[i]]:
#         graph[i].append(-2)
#     elif parents[i] == -1:
#         continue
#     else:
#         graph[parents[i]].append(i)

# print(graph.count([]))
###############################################
import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)
