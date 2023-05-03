import sys
bill = int(sys.stdin.readline())
n = int(sys.stdin.readline())
coins = []
total = []
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    total.append([x, y])

global count
count = 0

def DFS(z, sum) :
    global count
    if sum > bill :
        return
    if z == n :
        if sum == bill :
            count+=1
        return
    for j in range(total[z][1]+1) :
        DFS(z+1, sum+(total[z][0]*j))

DFS(0, 0)
print(count)