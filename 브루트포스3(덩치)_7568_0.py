import sys

N= int(sys.stdin.readline())
lst = []

for n in range(N) :
    w = list(map(int, sys.stdin.readline().split()))
    w.append(None)
    lst.append(w)

for n in range(N) :
    rank=[]
    r = 0
    u= 1
    if lst[n][2] == None :

        for i in range(N) :
            a = lst[n]
            b = lst[i]
            if a[0]<b[0] and a[1]<b[1]:
                u+=1
            else :
                pass
        lst[n][2]=u
    else : pass
answer = []
for n in range(N) :
   answer.append(lst[n][2])

print(' '.join(map(str, answer)))