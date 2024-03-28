def BackTracking(start,visit,S,B):
    global MIN_S_B


    if B!=0:
        MIN_S_B=min(MIN_S_B , abs(S-B) )

    for i in range(start,N):
        if not visit[i]:
            visit[i]=True
            BackTracking(start+1,visit , S*taste[i][0] , B+taste[i][1] )
            visit[i]=False

N=int(input())

taste=[ list(map(int,input().split())) for _ in range(N) ]
visit=[False]*N

MIN_S_B=int(1e9)

BackTracking(0,visit,1,0)
print(MIN_S_B)
