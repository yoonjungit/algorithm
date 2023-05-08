import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

now = [0, 0]

graph_check = [[True]*n for _ in range(n)]

max_zone = 0 
global zone
zone = 0

def BFS(z) :
    global zone
    graph_check[z[0]][z[1]] = False
    for i in range(4) :
        x = z[0] + dx[i]
        y = z[1] + dy[i]
        if 0<=x<n and 0<=y<n and graph[x][y] >= height and graph_check[x][y] == True:
            BFS([x, y])

for h in range(1, 101) :
    height = h
    graph_check = [[True]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if graph_check[i][j] == True and graph[i][j] >= height :
                BFS([i, j])
                zone+=1

    if zone == 0 :
        print(max_zone)
        exit(0)
    elif zone > max_zone :
        max_zone = zone
    zone = 0

print(max_zone)