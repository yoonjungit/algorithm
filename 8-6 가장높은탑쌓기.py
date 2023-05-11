import sys

n = int(input())
bricks = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

bricks.sort(key=lambda x : x[0])

under = [0]*n
under[0] = bricks[0][1]

for i in range(1, n) :
    max_under = 0
    for j in range(i-1, -1, -1) :
        if bricks[i][2]>bricks[j][2] and under[j]>max_under:
            max_under = under[j]
    under[i] = max_under+bricks[i][1]

print(max(under))