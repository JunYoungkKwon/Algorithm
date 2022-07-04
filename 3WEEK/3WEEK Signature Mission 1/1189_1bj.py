R,C,K = map(int,input().split()) #R,C,K를 받아줌
board = [input() for _ in range(R)] #board를 받아줌
board.reverse()
visited = [[False]*C for _ in range(R)] #방문했는지 하지 않았는지 받아줌

#좌표 평면에서 이동 가능한 가지 수를 받아줌(동남서북)
dx = [1,0,-1,0]
dy = [0,-1,0,1]

#유효한 좌표 평면인지 확인해 줌
def coord(y,x):
  return 0<=y<R and 0<=x<C

ans = 0 #정답을 받아줌
def dfs(start_y,start_x,dist):
  global ans
  #목표 지점이고, 해당하는 거리가 k일 때, 정답에 추가해줌
  if start_y == R-1 and start_x == C-1 and dist == K-1 and board[start_y][start_x] == '.':
    ans += 1
  else: #해당 Queue에 있는 좌표를 탐색
    visited[start_y][start_x] = True #방문했다고 처리해줌
    for i in range(4): #좌표 평면에서 이동 가능한 지점으로 이동해줌
      ny = start_y + dy[i]
      nx = start_x + dx[i]
      if coord(ny,nx) and board[ny][nx] == '.' and not visited[ny][nx]:
        dfs(ny,nx,dist+1)
    visited[start_y][start_x] = False #방문 기록을 초기화 시켜줌

dfs(0,0,0) #시작 지점에서 dfs를 시작함
print(ans) #정답을 출력함