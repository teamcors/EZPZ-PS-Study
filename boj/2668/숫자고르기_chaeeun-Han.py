# 15min 42sec
import sys
input = sys.stdin.readline

# 순환을 찾아서 result에 append하자
# 방문했던 노드를 다시 방문할 때 순환이 발생
def dfs(v,i):
    visited[v]=True
    w=data[v]
    if not visited[w]:
        dfs(w,i)
    elif visited[w] and w==i:
        result.append(w)
      
n=int(input())
data=[0]+[int(input()) for _ in range(n)]
result=[]

for i in range(1,n+1):
    visited=[False]*(n+1)
    dfs(i,i)
print(len(result))

result.sort()

for i in result:
    print(i)
