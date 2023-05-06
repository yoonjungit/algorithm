import sys

n = int(sys.stdin.readline())
mountain = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]

board = [[True]*n for _ in range(n)]

min_ = mountain[0][0]
max_ = mountain[0][0]

start = [0, 0]
end = [0, 0]


for i in range(n) :
    for j in range(n) :
        if mountain[i][j]>max_ :
            max_ = mountain[i][j]
            end = [i, j]
        if mountain[i][j]<min_ :
            min_ = mountain[i][j]
            start = [i, j]

board[start[0]][start[1]] = False

global count 
count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(z) :
    global count
    if z[0] == end[0] and z[1] == end[1] :
        count +=1
        return
    for i in range(4) :
        x = z[0]+dx[i]
        y = z[1]+dy[i]
        if 0<=x<n and 0<=y<n and mountain[x][y]>mountain[z[0]][z[1]] and board[x][y]==True :
            board[x][y]=False
            DFS([x, y])
            board[x][y]=True

DFS(start)
print(count)