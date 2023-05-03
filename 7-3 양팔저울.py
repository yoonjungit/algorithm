import sys

K = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))

weight = []
def DFS(x, w) :
    if x == K :
        if sum(N) >= w > 0 :
            weight.append(w)
        return
    else :
        DFS(x+1, w+N[x])
        DFS(x+1, w-N[x])
        DFS(x+1, w)


DFS(0, 0)
print(sum(N) - len(set(weight)))