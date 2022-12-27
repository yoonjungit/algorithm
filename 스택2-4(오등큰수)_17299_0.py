# 시간초과
import sys

N=int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split()))
F = dict()

for n in range(N) :
    i = stack[n]
    if i in F:
        F[i]+=1
    else :
        F[i] = 1

answer = []
for n in range(N) :
    i = n
    val = stack[n]
    t = []
    while i < N :
        a = stack[i]
        if F[a]>F[val] :
            answer.append(a)
            i = N
    if len(answer) == n :
        answer.append(-1)

print(" ".join(map(str, answer)))