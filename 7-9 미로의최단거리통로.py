import sys
from collections import deque
miro = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]

miro[0][0] = 1

Q = deque()
Q.append((0, 0))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = [[0]*7 for _ in range(7)]

while Q :
    tmp=Q.popleft()
    for i in range(4) :
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and miro[x][y]==0 :
            miro[x][y]=1
            board[x][y] = board[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if board[6][6]== 0:
    print(-1)
else :
    print(board[6][6])