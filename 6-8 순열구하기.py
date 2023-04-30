import sys
N, M = map(int, input().split())
marble = list(range(1, N+1))
res = [0]*M
global count
count = 0

def DFS(x, marble) :
    global count
    if x >= M :
        print(' '.join(res))
        count+=1
        return
    for y in range(len(marble)) :
        res[x] = str(marble[y])
        DFS(x+1, marble[0:y]+marble[y+1:len(marble)])

DFS(0, marble)
print(count)