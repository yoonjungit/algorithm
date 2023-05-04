import sys

n, m = map(int, sys.stdin.readline().split())


global min_jump

min_jump = m-n
if min_jump < 0 :
    min_jump = n-m

def DFS(x, jump) :
    global min_jump
    if x == m :
        if min_jump>jump :
            min_jump = jump
        return
    if jump > min_jump :
        return
    if n>m :
        print(min_jump)
        exit(0)
    (m-n)//5 
    DFS(x+5, jump+1)
    DFS(x-1, jump+1)
    DFS(x+1, jump+1)

if n>m :
    print(min_jump)
    exit(0)

five_jump = (m-n)//5
min_jump = five_jump + (m-(five_jump*5+n))
DFS(five_jump*5+n, five_jump)

print(min_jump)