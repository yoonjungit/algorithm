import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

count = 0

def BFS(z) :
    for i in range(8) :
        x = z[0]+dx[i]
        y = z[1]+dy[i]
        if 0<=x<n and 0<=y<n and board[x][y] == 1 :
            board[x][y] = 0
            BFS([x, y])
    
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 :
            board[i][j] = 0
            BFS([i, j])
            count += 1

print(count)