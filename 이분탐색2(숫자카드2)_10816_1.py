# 시간초과
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

c = 0
def find(x, start, end) :
    c = 0
    while True : 
        if x < A[0] or x>A[N-1] or start > end :
            return 0
        h = (start+end)//2
        half = A[h]
        if x < half :
            return find(x, start, h-1)
        elif x > half :
            return find(x, h+1, end)
        else :
            c+=1
            h_s = h
            while h>0 :
                if A[h]==A[h-1] :
                    h-=1
                else : 
                    break
            if h_s - h > 0 :
                c += h_s-h
            h = h_s
            while h<len(A)-1 :
                if A[h]==A[h+1] :
                    h+=1
                else :
                    break
            if h - h_s > 0 :
                c += h-h_s            
            return c
ans = []
for x in B :
    ans.append(find(x,0,N))

print(' '.join(map(str, ans)))
