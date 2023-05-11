import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

power = [[0]*n for _ in range(n)]
power[0][0] = graph[0][0]

# 1. bottom-up
for i in range(1, n) :
    power[i][0] = graph[i][0]+power[i-1][0]
    power[0][i] = graph[0][i]+power[0][i-1]


for i in range(1, n) :
    for j in range(1, n) :
        power[i][j] = min(power[i-1][j], power[i][j-1]) + graph[i][j]

print(power[n-1][n-1])

dy = [[0]*n for _ in range(n)]
dy[0][0] = graph[0][0]

# 2. top-down
def recursive(x, y) :
    if dy[x][y] != 0 :
        return dy[x][y]
    
    elif x==0 or y==0 :
        if x == 0 :
            dy[x][y] = recursive(x, y-1) + graph[x][y]
        else :
            dy[x][y] = recursive(x-1, y) + graph[x][y]
    
    else : dy[x][y] = min(recursive(x-1, y), recursive(x, y-1))+graph[x][y]
    return dy[x][y]

# recursive(n-1, n-1)

# print(dy[n-1][n-1])