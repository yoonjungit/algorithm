import sys

n = int(sys.stdin.readline())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

half = n//2 

total = 0 

for x in range(half+1) :
    if x < half :
        total+=sum(farm[x][half-x:half+x+1])
        total+=sum(farm[(n-1)-x][half-x:half+x+1])
    else:
        total+=sum(farm[x])

print(total)