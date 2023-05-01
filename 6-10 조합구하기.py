import sys

N, M = map(int, sys.stdin.readline().split())

marble = list(range(1, N+1))

global count
count = 0

res = [0]*M

def DFS(marble, L) :
    global count
    if L >= M :
        print(' '.join(res))
        count+=1
    else :
        for x in range(len(marble)) :
            res[L] = str(marble[x])
            DFS(marble[x+1:], L+1)

DFS(marble, 0)
print(count)