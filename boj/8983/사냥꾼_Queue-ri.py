import sys
input = sys.stdin.readline

def solution():
    m, n, l = map(int, input().split())
    sade = list(map(int, input().split()))
    sade = sorted(sade)
    anim_pos = []
    for _ in range(n):
        x, y = map(int, input().split())
        anim_pos.append((x, y))
    
    cnt = 0
    for a in anim_pos:
        r1, r2 = a[0]+a[1]-l, a[0]-a[1]+l
        mn, mx = 0, len(sade)-1
        while mn <= mx:
            md = (mn + mx) // 2
            
            if r1 <= sade[md] <= r2:
                cnt += 1
                break
            else:
                if sade[md] < r1:
                    mn = md + 1
                else:
                    mx = md - 1
        
    print(cnt)
    
if __name__ == '__main__':
    solution()
