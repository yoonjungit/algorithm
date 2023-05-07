import sys

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range(n)]

global count
count = 0
res = []


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]



def BFS(z) :
    global count

    for i in range(4) :
        x = z[0]+dx[i]
        y = z[1]+dy[i]
        if 0<=x<n and 0<=y<n and board[x][y] == '1' :
            board[x][y] = 0
            count+=1
            BFS((x, y))

for i in range(n) :
    for j in range(n) :
        if board[i][j] == '1':
            board[i][j] = 0
            count+=1
            BFS((i, j))
            res.append(count)
            count=0

print(len(res))
res.sort()
for i in res :
    print(i)