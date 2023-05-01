import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(range(1, N+1))

global answer
answer = 0 

def DFS(num, first_row) :
    global answer
    if len(first_row) >= N :
        sum = 0
        for i in range(len(first_row)) :
            sum+= first_row[i]*b[i]
        if sum == M :
            for x in first_row :
                print(x, end = ' ')
            exit(0)
    else :
        for i in range(len(num)) :
            first_row.append(num[i])
            DFS(num[0:i] + num[i+1:], first_row)
            first_row.pop()

b=[1]*N
for i in range(1, N-1) :
    b[i] = b[i-1]*(N-i)//i

DFS(num_list, [])