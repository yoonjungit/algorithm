def ripe(z) :
    for i in range(4):
        x = dx[i] + z[0]
        y = dy[i] + z[1]
        if 0<=x<height and 0<=y<width and tomatoes[x][y] == 0 :
            tomatoes[x][y] = 2


import sys
sys.setrecursionlimit(10**6)

width, height = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, (sys.stdin.readline().split()))) for _ in range(height)]

yesterday = [[False]*width for _ in range(height)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start = [0, 0]

day = 0
while True :
    day+=1
    cnt = 0

    for i in range(height) :
        for j in range(width) :
            if tomatoes[i][j] == 1:
                ripe([i, j])
    
    for i in range(height) :
        for j in range(width) :
            if tomatoes[i][j] == 2:
                cnt+= 1
                tomatoes[i][j] = 1

    if cnt == 0 :
        break


for i in range(height) :
    for j in range(width) :
        if tomatoes[i][j] == 0 :
            print(-1)
            exit(0)

print(day-1)