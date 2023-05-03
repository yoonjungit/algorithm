import sys

n = int(sys.stdin.readline())

coins = list(map(int, sys.stdin.read().split()))

global find_min
find_min=max(coins)

def DFS(x, sum) :
    global find_min
    if x >= n :
        if len(sum) == len(set(sum)) and find_min > max(sum)-min(sum) :
            find_min = max(sum)-min(sum)
        return
    for i in range(3) :
        sum[i] += coins[x]
        DFS(x+1, sum)
        sum[i] -= coins[x]

DFS(0, [0, 0, 0])

print(find_min)