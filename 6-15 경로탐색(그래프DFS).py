import sys
N, M = map(int, sys.stdin.readline().split())

adjacent_matrix = [[0]*N for _ in range(N)]

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    adjacent_matrix[x-1][y-1] = 1

route_arr = [1]
global count
count = 0

def route(x) :
    global count
    if x == N-1 :
        count += 1
        return
    for j in range(N) :
        if adjacent_matrix[x][j] == 1 and j+1 not in route_arr:
            route_arr.append(j+1)
            route(j)
            route_arr.pop()

route(0)
print(count)