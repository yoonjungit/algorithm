import sys
miro = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]

miro[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

global count
count = 0

def DFS(z, w) :
    global count
    if z == 6 and w == 6:
        count +=1
        return
    for i in range(4) :
        x = z+dx[i]
        y = w+dy[i]
        if 0<=x<=6 and 0<=y<=6 and miro[x][y]==0 :
            miro[x][y] = 1
            DFS(x, y)
            miro[x][y] = 0

DFS(0, 0)
print(count)