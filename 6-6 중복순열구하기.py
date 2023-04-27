import sys
N, M = map(int, sys.stdin.readline().split())
round = list(range(1, N+1))
global answer
answer = 0
res = [0]*M

def get_list(L):
    global answer
    if L==M :
        print(' '.join(res))
        answer+=1
        return 
    for x in range(1, N+1) :
        res[L]= str(x)
        get_list(L+1)


get_list(0)
print(answer)