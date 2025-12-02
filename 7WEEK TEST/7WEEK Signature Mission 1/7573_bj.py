import sys
input = sys.stdin.readline
N,L,M = map(int,input().split())
fish=[]

# 그물의 크기별로 구하는 함수
def getNet(nL):
    half_nL= nL//2
    nets=[]
    for i in range(1,half_nL):
        nets.append((i,half_nL-i))
    return nets

#그물을 칠 수 있는 범위 chk
# zero-base가 아니기 때문에, N 포함 xx
def is_valid_coord(y,x,net):
    if y+net[0]>N or x+net[1]>N:
        return False
    else:
        return True
# 그물의 범위 안에, 물고기들이 몇마리가 있는지 확인해준다.
def cntFish(y,x,net):
    if not is_valid_coord(y,x,net):
        return 0
    fcnt= 0
    for fh in fish:
        fy,fx=fh
        if y<=fy<=y+net[0] and x<=fx<=x+net[1]:
            fcnt+=1
    return fcnt

def getFish(net):
    maxfish=0
    for fh in fish:
        y,x = fh
        for ny in range(y,y-net[0]-1,-1):
            maxfish=max(maxfish,cntFish(ny,x,net))
        for nx in range(x,x-net[1]-1,-1):
            maxfish=max(maxfish,cntFish(y,nx,net))
    return maxfish

for _ in range(M):
    y,x=map(int,input().split())
    fish.append((y,x))

def solve():
    nets = getNet(L)
    ans=0
    for net in nets:
        ans =max(ans,getFish(net))
    print(ans)

solve()