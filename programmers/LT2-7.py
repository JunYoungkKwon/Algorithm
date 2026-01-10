# [벡준] 스타트택시
N,M,stat_fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
s_y,s_x = map(int, input().split())
passenger = []
for _ in range(2,M+2):
    p_y, p_x, t_y, y_x = map(int, input().split())
    passenger.append((p_y, p_x, t_y, y_x))

print(passenger)
