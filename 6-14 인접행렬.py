import sys
N, M = map(int, sys.stdin.readline().split())
nodes = []
for _ in range(M) :
    nodes.append(list(map(int, input().split())))

adjacent_nodes = [['0']*N for _ in range(N)]

for x in nodes :
    adjacent_nodes[x[0]-1][x[1]-1] = str(x[2])

for x in adjacent_nodes :
    print(' '.join(x))