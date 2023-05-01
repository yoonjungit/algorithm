import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(range(1, N+1))

global answer
answer = 0 

def DFS(num, first_row) :
    global answer
    if len(first_row) >= N :
        check(first_row)
        if answer == 1 :
            for x in first_row : 
                print(x, end = ' ')
            exit(0)
    else :
        for i in range(len(num)) :
            first_row.append(num[i])
            DFS(num[0:i] + num[i+1:], first_row)
            first_row.pop()

def check(first_row) :
    global answer
    temp = []
    if len(first_row) == 2 :
        if sum(first_row) == M :
            answer = 1
        return
    else : 
        for x in range(len(first_row)-1) :
            temp.append(first_row[x]+first_row[x+1])
        return check(temp)

DFS(num_list, [])