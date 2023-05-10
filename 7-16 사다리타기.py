import sys
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

end_point = 0
for i in range(10) :
    if graph[9][i] == 2 :
        end_point = i
        break

dx = [0, 0, -1]
dy = [1, -1, 0]

def BFS(z) :
    for i in range(3) :
        if z[0] == 0 :
            print(z[1])
            exit(0)
        x = z[0] + dx[i]
        y = z[1] + dy[i]
        if 0<=x<10 and 0<=y<10 and graph[x][y] == 1 :
            graph[x][y] = 3
            BFS([x, y])

BFS([9, end_point])